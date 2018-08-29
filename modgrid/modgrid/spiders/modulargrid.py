# -*- coding: utf-8 -*-
import scrapy

from ..items import ModGridItem


class ModulargridSpider(scrapy.Spider):
    name = 'modulargrid'
    allowed_domains = ['modulargrid.net']
    start_urls = [
        'https://www.modulargrid.net/e/modules/find/page:1?SearchName=&SearchVendor=&SearchFunction=&SearchSecondaryfunction=&SearchTe=&SearchTemethod=max&SearchBuildtype=&SearchLifecycle=&SearchSet=all&SearchMarketplace=&SearchIsmodeled=0&SearchShowothers=1&SearchShow1u=0&order=newest&direction=asc'
    ]

    def parse(self, response):
        items = response.css('.container .box-module')

        for item in items:
            obj = ModGridItem()
            obj['manufacturer'] = item.css(
                'h4.module-name a::text').extract_first()
            obj['name'] = item.css('h3.module-name::text').extract_first()
            url = item.css(
                '.elements-bottom .btn-toolbar a:nth-of-type(2)::attr(href)'
            ).extract_first()
            obj['url'] = response.urljoin(url)
            obj['price'] = item.xpath(
                './/span[@class="price"]/span[contains(@class, "currency")]/text()'
            ).extract_first()
            obj['tags'] = item.xpath(
                './/div[@class="module-tags"]//span/text()').extract()
            yield obj

        # find next page
        next_page_url = response.css(
            '#box-paginator .paging .next a::attr(href)').extract_first()

        if next_page_url:
            next_page_url = response.urljoin(next_page_url)
            yield scrapy.Request(next_page_url)
