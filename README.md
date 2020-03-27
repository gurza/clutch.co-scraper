clutch.co scraper
=================

Scrape web developers from [https://clutch.co/web-developers]().

Datapoints:
* Company name
* Location
* Website
* Av hourly rate
* Employees
* Founded date
* Service lines (TOP3)
* Frameworks & CMS (TOP3)

Data is parsed from HTML and JS scripts.

## Install and run
```console
$ pip install -r requirements.txt
$ scrapy runspider webdev_spider.py -o out/webdev.json
$ scrapy runspider profile_spider.py -o out/profiles.csv
```
