# ProthomAloScraper

A python script to scrape all article with title, category, summary (if available) and URL from Prothom Alo

To get help run:
`python scraper.py -h` or `python scraper.py --help`

Documentation:

```
usage: python scraper.py [-h] [--write-interval WRITE_INTERVAL]
                         [--verbose VERBOSE]
                         start end filename

Scrape articles from Prothom Alo

positional arguments:
  start                 Starting article ID from Prothom Alo
  end                   Ending article ID from Prothom Alo
  filename              Filename for the csv file

optional arguments:
  -h, --help            show this help message and exit
  --write-interval WRITE_INTERVAL
                        Write to file after every interval (default 25)
  --verbose VERBOSE     0 = False, 1 = True (default 1)

```

Give an starting id, ending id and a filename, the script will scrape all the articles from given ID and save them to filename.csv
