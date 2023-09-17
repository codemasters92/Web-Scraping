
#TODO === 1° - Site Books === ok
# aula 27 -> 31
#? === 1° Primeira resolução ===
# import scrapy
# import re
# import os


# class MainSpider(scrapy.Spider):
#     name = "main"
#     start_urls = ["http://books.toscrape.com/index.html"]

#     def parse(self, response, **kwargs):
#         links = response.xpath('//h3/a/@href')
#         for link in links:
#             yield response.follow(link, callback=self.parse_book)
        
#         if next_page := response.xpath('//li[@class="next"]/a/@href').get():
#             yield response.follow(next_page,callback=self.parse)
        
#     def parse_book(self, response):
#         title = response.xpath('//h1//text()').get()
#         price = response.xpath('//p[@class="price_color"]//text()').get()
#         stock = response.xpath('//p[@class="instock availability"]//text()').getall()
#         stock = [i for i in stock if 'available' in i][0].strip()
#         rating = response.xpath('//p[contains(@class,"star-rating")]/@class').get().split()[-1]
#         url = response.url
#         img = 'http://books.toscrape.com/' + response.xpath('//div[@class="thumbnail"]//img/@src').get().split('..')[-1]
#         upc = response.xpath('//table//td//text()').get()
#         reviews = response.xpath('//table//tr[last()]/td/text()').get()
#         tag = response.xpath('//ul//li[last() - 1]/a/text()').get()
        
#         yield {
#             'title' : title,
#             'price' : price,
#             'stock' : stock,
#             'rating' : rating,
#             'url' : url,
#             'img' : img,
#             'upc' : upc,
#             'reviews' : reviews,
#             'tag' : tag
#         }

#         yield scrapy.Request(url=img, callback=self.parse_img, cb_kwargs={'title' : title})


#     def parse_img(self, response, title):
#         # Substitui caracteres inválidos por espaços em branco no título do livro
#         substitui_caracteres = re.sub(r'[\/:*?"<>|]', ' ', title)

#         # Cria o nome do arquivo com o título sanitizado e a extensão ".jpg"
#         file_name = f'./imgs/{substitui_caracteres}.jpg'

#         # Garante que o diretório ./imgs/ exista
#         os.makedirs(os.path.dirname(file_name), exist_ok=True)

#         with open(file_name, 'wb') as file:
#             file.write(response.body)



#? === 2° Segunda resolução ===
#Aula 31 -> 39
import scrapy
from ..items import BooksItem


class MainSpider(scrapy.Spider):
    name = "books"
    start_urls = ["http://books.toscrape.com/index.html"]

    def parse(self, response, **kwargs):
        links = response.xpath('//h3/a/@href')
        for link in links:
            yield response.follow(link, callback=self.parse_book)
        
        if next_page := response.xpath('//li[@class="next"]/a/@href').get():
            yield response.follow(next_page,callback=self.parse)
        
    def parse_book(self, response):
        item = BooksItem()
        item['title'] = response.xpath('//h1//text()').get()
        item['price'] = response.xpath('//p[@class="price_color"]//text()').get()
        stock = response.xpath('//p[@class="instock availability"]//text()').getall()
        item['stock'] = [i for i in stock if 'available' in i][0].strip()
        item['rating'] = response.xpath('//p[contains(@class,"star-rating")]/@class').get().split()[-1]
        item['url'] = response.url
        item['image_urls'] = ['http://books.toscrape.com/' + response.xpath('//div[@class="thumbnail"]//img/@src').get().split('..')[-1]]
        item['upc'] = response.xpath('//table//td//text()').get()
        item['reviews'] = response.xpath('//table//tr[last()]/td/text()').get()
        item['tag'] = response.xpath('//ul//li[last() - 1]/a/text()').get()
        
        yield item


