# -*- coding: utf-8 -*-
import os
import re
import json

import scrapy
import ijson


here = os.path.dirname(os.path.abspath(__file__))
companies_file = os.path.join(here, 'out', 'webdev.json')
companies = ijson.items(open(companies_file), 'item')


class ProfileSpider(scrapy.Spider):
    name = 'profile'
    start_urls = [next(companies)['url']]

    def parse(self, response):
        # Extract js data
        settings_script = response.xpath('//script/text()').getall()[-1]
        settings = json.loads(
            re.findall('jQuery.extend\(Drupal.settings, (.*)\);', settings_script)[0]
        )

        # Collect service lines and frameworks
        services = list()
        frameworks = list()
        for chart in response.css('div.field-group-chart-wrapper'):
            char_title = chart.css('div.h3_title::text').get()
            chart_id = chart.css('div.chartAreaWrapper::attr(id)').get()
            graph = list(
                filter(lambda graph: graph.get('element_id') == chart_id, settings.get('clutchGraph', list()))
            )[0]
            if char_title == 'Service lines':
                services = [
                    {
                        'label': ds.get('label'),
                        'value': ds.get('value'),
                    }
                    for ds in graph.get('dataset', list())]
            elif char_title == 'Frameworks and CMS':
                frameworks = [
                    {
                        'label': ds.get('label'),
                        'value': ds.get('value'),
                    }
                    for ds in graph.get('dataset', list())]

        yield {
            'Company name': response.css('h1.page-title::text').get().strip(),
            'Location': response.css('div.quick-menu ul.nav-stacked div.city-name::text').get(),
            'Website': response.css('div.quick-menu ul.nav-stacked li.website-link-a a::attr(href)').get(),
            'Av hourly rate': response.css('div.field-name-field-pp-hrly-rate-range div.field-item::text').get(),
            'Employees': response.css('div.field-name-field-pp-size-people div.field-item::text').get(),
            'Founded date':
                'Undisclosed' if response.css('div.field-name-field-pp-year-founded').css('.undisclosed')
                else response.css('div.field-name-field-pp-year-founded div.field-item::text').get(),
            # TOP-3 Service lines
            'Service 1':         services[0].get('label') if len(services) > 0 else None,
            'Service 1 - share': services[0].get('value') if len(services) > 0 else None,
            'Service 2':         services[1].get('label') if len(services) > 1 else None,
            'Service 2 - share': services[1].get('value') if len(services) > 1 else None,
            'Service 3':         services[2].get('label') if len(services) > 2 else None,
            'Service 3 - share': services[2].get('value') if len(services) > 2 else None,
            # TOP-3 Frameworks and CMS
            'Framework 1':         frameworks[0].get('label') if len(frameworks) > 0 else None,
            'Framework 1 - share': frameworks[0].get('value') if len(frameworks) > 0 else None,
            'Framework 2':         frameworks[1].get('label') if len(frameworks) > 1 else None,
            'Framework 2 - share': frameworks[1].get('value') if len(frameworks) > 1 else None,
            'Framework 3':         frameworks[2].get('label') if len(frameworks) > 2 else None,
            'Framework 3 - share': frameworks[2].get('value') if len(frameworks) > 2 else None,
        }

        try:
            next_page = next(companies)['url']
            yield response.follow(next_page)
        except StopIteration:
            pass
