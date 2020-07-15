import bs4
import requests
import argparse
import sys
import pandas as pd

parser = argparse.ArgumentParser(prog="python scraper.py", description='Scrape articles from Prothom Alo')
parser.add_argument('start', type=int, help='Starting article ID from Prothom Alo')
parser.add_argument('end', type=int, help='Ending article ID from Prothom Alo')
parser.add_argument('filename', help='Filename for the csv file')

start, end, filename = parser.parse_args().start, parser.parse_args().end, parser.parse_args().filename
if start <= 0:
  print("Start ID should be at least 1.")
  sys.exit()

def get_article_by_id(id):
  url = f"https://www.prothomalo.com/bangladesh/article/{id}"
  res = requests.get(url)
  soup = bs4.BeautifulSoup(res.content, "html.parser")
  try:
    title = soup.find("title").text
    category = soup.find("a", {"class":"category_name"}).text.split()[0]
    article_div = soup.find("div", {"itemprop":"articleBody"})
    paragraphs = []
    for p in article_div.find_all("p"):
      if p.find("strong") and p.find("strong").text == "আরও পড়ুন":
        break
      paragraphs.append(p.text)
    article = ' '.join(paragraphs)
    article_dict = {
        "url": url,
        "title": title,
        "category": category,
        "article": article
    }
  except:
    return -1

  return article_dict

articles = []
write_interval=10
header=True

for id in range(start, end):
  article = get_article_by_id(id)
  if article != -1:
    articles.append(article)
  if id % write_interval == 0:
    dataframe = pd.DataFrame(articles)
    dataframe.to_csv(f"{filename}.csv", index=False, mode="a", header=header)
    header=False
    print(f"ID {start} to {id} is written to file")
    articles = []
