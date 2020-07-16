import bs4
import requests
import argparse
import sys
import os
import pandas as pd

parser = argparse.ArgumentParser(prog="python scraper.py", description='Scrape articles from Prothom Alo')
parser.add_argument('start', type=int, help='Starting article ID from Prothom Alo')
parser.add_argument('end', type=int, help='Ending article ID from Prothom Alo')
parser.add_argument('filename', help='Filename for the csv file')
parser.add_argument('--write-interval', type=int, help='Write to file after every interval (default 25)')
parser.add_argument('--verbose', type=int, help='0 = False, 1 = True (default 1)')
args = parser.parse_args()

start, end, filename = args.start, args.end, args.filename
write_interval = 25 if args.write_interval == None else args.write_interval
verbose = 1 if args.verbose == None else args.verbose

if start <= 0:
  print("Start ID should be at least 1.")
  sys.exit()

def get_article_by_id(id):
  url = f"https://www.prothomalo.com/bangladesh/article/{id}"
  res = requests.get(url)
  soup = bs4.BeautifulSoup(res.content, "html.parser")
  try:
    title = soup.find("title").text
    summary = soup.find("meta", {"name":"description"})["content"]
    category = soup.find("a", {"class":"category_name"}).text.split()[0]
    article_div = soup.find("div", {"itemprop":"articleBody"})
    paragraphs = []
    for p in article_div.find_all("p"):
      if p.find("strong") and p.find("strong").text == "আরও পড়ুন":
        break
      paragraphs.append(p.text)
    article = ' '.join(paragraphs)
    article = article.replace('\n', ' ')
    article_dict = {
        "url": url,
        "category": category,
        "title": title,
        "summary": summary,
        "article": article
    }
  except:
    return -1

  return article_dict

articles = []
header=(not (os.path.exists(filename) and os.stat(filename).st_size))
counter=0

for id in range(start, end):
  article = get_article_by_id(id)
  if article != -1:
    articles.append(article)
    counter = counter + 1

  if counter % write_interval == 0:
    dataframe = pd.DataFrame(articles)
    dataframe.to_csv(f"{filename}", index=False, mode="a", header=header)
    header=False
    if verbose > 0:
      print(f"{counter} articles(ID: {start}-{id}) written to file")
    articles = []

print(f"Operation Complete!\n{counter} articles were written to {filename}")