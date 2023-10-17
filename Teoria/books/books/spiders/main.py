
#TODO === 1° - Site Books === 
#? === 1- Baixando imagens === 
#** === 1° Primeira resolução === 
# aula 27 -> 29
# Baixando as imagens manualmente usando o nome do livro. (resulta em problemas de caracteres que devem ser tratados.)
# import scrapy
# import re
# import os


# class MainSpider(scrapy.Spider):
#     name = "books"
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


#** === 2° Segunda resolução === 
#Aula 32
# Baixando as imagens manualmente usando o url do livro.
# import scrapy
# import re
# import os

# class MainSpider(scrapy.Spider):
#     name = "books"
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

#         yield scrapy.Request(img, callback=self.parse_img, cb_kwargs={'filename' : url})

#     def parse_img(self, response, filename):
#         filename = filename.split('/')[-2]
#         with open (f'imgs/{filename}.jpg', 'wb') as file:
#             file.write(response.body)


#** === 3° Terceira resolução === 
#Aula 31 
#Baixando as imagens pelo scrapy images pipeline (sem o nome original das imagens).
# import scrapy
# from ..items import BooksItem

# class MainSpider(scrapy.Spider):
#     name = "books"
#     start_urls = ["http://books.toscrape.com/index.html"]

#     def parse(self, response, **kwargs):
#         links = response.xpath('//h3/a/@href')
#         for link in links:
#             yield response.follow(link, callback=self.parse_book)
        
#         if next_page := response.xpath('//li[@class="next"]/a/@href').get():
#             yield response.follow(next_page,callback=self.parse)
        
#     def parse_book(self, response):
#         item = BooksItem()
#         item['title'] = response.xpath('//h1//text()').get()
#         item['price'] = response.xpath('//p[@class="price_color"]//text()').get()
#         stock = response.xpath('//p[@class="instock availability"]//text()').getall()
#         item['stock'] = [i for i in stock if 'available' in i][0].strip()
#         item['rating'] = response.xpath('//p[contains(@class,"star-rating")]/@class').get().split()[-1]
#         item['url'] = response.url
#         item['image_urls'] = ['http://books.toscrape.com/' + response.xpath('//div[@class="thumbnail"]//img/@src').get().split('..')[-1]]
#         item['upc'] = response.xpath('//table//td//text()').get()
#         item['reviews'] = response.xpath('//table//tr[last()]/td/text()').get()
#         item['tag'] = response.xpath('//ul//li[last() - 1]/a/text()').get()
        
#         yield item

#** === 4° Quarta resolução === 
#Aula 33 a 39
#Baixando as imagens de pipeline criada (com o nome original das imagens).
import scrapy.pipelines.images


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


#TODO === 2° - Entendendo pipelines === 
#? === Pipeline original do scrapy
#? === Pipeline criada para salvar as imagens com o nome
#? === Pipeline criada para salvar os dados em um banco de dados.
#? === Pipeline criada para salvar os dados em um banco de dados com ORM peewee.
#? === Pipeline criada para salvar os dados em um banco de dados com MongoDB.

#TODO === 3° - Configurando pipelines === 
#? === Configuraçoes basica de pipelines.
#? === Configuraçoes basica de pipelines globais.
#? === Configuraçoes basica de pipelines locais.




