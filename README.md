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


## Data sample
```console
$ head out/webdev.json
[
{"name": "MentorMate", "url": "https://clutch.co/profile/mentormate"},
{"name": "Experion Technologies", "url": "https://clutch.co/profile/experion-technologies"},
{"name": "Capital Numbers", "url": "https://clutch.co/profile/capital-numbers"},
{"name": "CemtrexLabs", "url": "https://clutch.co/profile/cemtrexlabs"},
{"name": "Unleashed Technologies", "url": "https://clutch.co/profile/unleashed-technologies"},
{"name": "Iflexion", "url": "https://clutch.co/profile/iflexion"},
{"name": "10Clouds", "url": "https://clutch.co/profile/10clouds"},
{"name": "IT CRAFT", "url": "https://clutch.co/profile/it-craft"},
{"name": "Boldare", "url": "https://clutch.co/profile/boldare"},

$ head -2 out/profiles.csv 
Company name,Location,Website,Av hourly rate,Employees,Founded date,Service 1,Service 1 - share,Service 2,Service 2 - share,Service 3,Service 3 - share,Framework 1,Framework 1 - share,Framework 2,Framework 2 - share,Framework 3,Framework 3 - share
MentorMate,"Minneapolis, MN",https://mentormate.com/,$50 - $99 / hr,250 - 999,2001,Web Development,50,Custom Software Development,25,UX/UI Design,15,.NET,20,AngularJS,18,WordPress,8```
```
