# ProthomAloScraper
A python script to scrape all article from Prothom Alo

To get help run:
`python scraper.py -h` or `python scraper.py --help`

Documentation:
```
usage: python scraper.py [-h] start end filename

Scrape articles from Prothom Alo

positional arguments:
  start       Starting article ID from Prothom Alo
  end         Ending article ID from Prothom Alo
  filename    Filename for the csv file

optional arguments:
  -h, --help  show this help message and exit
```

Give an starting id, ending id and a filename, the script will scrape all the articles from given ID and save them to filename.csv
