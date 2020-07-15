# ProthomAloScrapper
A python script to scrap all article from Prothom Alo

To get help run:
`python scrap.py -h` or `python scrap.py --help`

Documentation:
```
usage: python scrap.py [-h] start end filename

Scrap articles from Prothom Alo

positional arguments:
  start       Starting article ID from Prothom Alo
  end         Ending article ID from Prothom Alo
  filename    Filename for the csv file

optional arguments:
  -h, --help  show this help message and exit
```

Give an starting id, ending id and a filename, the script will scrap all the articles from given ID and save them to filename.csv
