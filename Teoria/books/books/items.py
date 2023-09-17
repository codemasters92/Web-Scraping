# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BooksItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    price = scrapy.Field()
    stock = scrapy.Field()
    rating = scrapy.Field()
    url = scrapy.Field()
    upc = scrapy.Field()
    reviews = scrapy.Field()
    tag = scrapy.Field()
    image_urls = scrapy.Field()

