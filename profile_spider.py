# -*- coding: utf-8 -*-
import scrapy


class ProfileSpider(scrapy.Spider):
    name = 'profile'
    start_urls = ['https://clutch.co/profile/mencoweb-technologies',
                  'https://clutch.co/profile/hatcher-designs',]

    def parse(self, response):
        yield {
            'Company name': response.css('h1.page-title::text').get().strip(),
            'Location': response.css('div.quick-menu ul.nav-stacked div.city-name::text').get(),
            'Website': response.css('div.quick-menu ul.nav-stacked li.website-link-a a::attr(href)').get(),

        }
