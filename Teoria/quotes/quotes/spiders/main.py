
#TODO === 1° - Site Random quote ===
#? === 1° Primeira resolução ===
#* ====1.1° Scraping em 1 nivel.
# import scrapy

# class QuotesSpider(scrapy.Spider):
#     name = 'main'

#     start_urls = ['http://quotes.toscrape.com/random']

#     def parse(self, response):
#         quote = response.css('div.quote')
        
#         text = quote.css('span.text::text').get()
#         author = quote.css('span small::text').get()
#         tags = quote.css('div.tags a.tag::text').getall()

#         yield {
#             'text': text,
#             'author': author,
#             'tags': tags
#         }

#* ==== 1.2° Scraping em 2 nivel (duas paginas dentro do mesmo site).
# import scrapy

# class QuotesSpider(scrapy.Spider):
#     name = 'main'

#     start_urls = ['http://quotes.toscrape.com/random']

#     def parse(self, response):
#         quote = response.css('div.quote')
        
#         text = quote.css('span.text::text').get()
#         author = quote.css('span small::text').get()
#         tags = quote.css('div.tags a.tag::text').getall()
#         link = quote.xpath('.//small[@class="author"]/../a/@href').get()
#         yield scrapy.Request(f'https://quotes.toscrape.com{link}', dont_filter = True, callback = self.parse_total, cb_kwargs = {
#             'texto' : text,
#             'autor' : author,
#             'tags' : tags
#         })

#     def parse_total(self, response, texto, autor, tags):
#         autor_born_date = response.xpath('//span[@class="author-born-date"]/text()').get()
#         description = response.xpath('//div[@class="author-description"]/text()').get().strip()

#         yield {
#             'texto' : texto,
#             'autor' : autor,
#             'tags' : tags,
#             'autor_born_date' : autor_born_date,
#             'description' : description
#         }

#? === 2° Segunda resolução ===
#* ====2.1° Scraping em 1 nivel. 
# import scrapy

# class QuoteData(scrapy.Item):
# 	quote = scrapy.Field()
# 	author = scrapy.Field()
# 	tags = scrapy.Field()

# class QuoteDataSpider(scrapy.Spider):
# 	name = "main"

# 	start_urls = ['http://quotes.toscrape.com/random']

# 	def parse(self, response):

# 		quoteData = QuoteData()
# 		quoteBlocks = response.css('div.quote')
		
# 		quoteData['quote'] = quoteBlocks.css('span.text::text').get()
# 		quoteData['author'] = quoteBlocks.css('span small::text').get()
# 		quoteData['tags'] = quoteBlocks.css('div.tags a.tag::text').getall()
# 		yield quoteData	

#* ====2.2° Scraping em 2 nivel (duas paginas dentro do mesmo site).

# import scrapy

# class QuoteData(scrapy.Item):
#     quote = scrapy.Field()
#     author = scrapy.Field()
#     tags = scrapy.Field()
#     author_born_date = scrapy.Field()
#     description = scrapy.Field()

# class QuotesSpider(scrapy.Spider):
#     name = 'quotes'

#     start_urls = ['http://quotes.toscrape.com/random']

#     def parse(self, response):
#         quote = response.css('div.quote')
        
#         text = quote.css('span.text::text').get()
#         author = quote.css('span small::text').get()
#         tags = quote.css('div.tags a.tag::text').getall()
#         link = quote.xpath('.//small[@class="author"]/../a/@href').get()

#         yield scrapy.Request(f'https://quotes.toscrape.com{link}', dont_filter=True, callback=self.parse_total, cb_kwargs={
#             'text': text,
#             'author': author,
#             'tags': tags
#         })

#     def parse_total(self, response, text, author, tags):
#         author_born_date = response.xpath('//span[@class="author-born-date"]/text()').get()
#         description = response.xpath('//div[@class="author-description"]/text()').get().strip()

#         quoteData = QuoteData()
#         quoteData['quote'] = text
#         quoteData['author'] = author
#         quoteData['tags'] = tags
#         quoteData['author_born_date'] = author_born_date
#         quoteData['description'] = description

#         yield quoteData


#TODO === 2° - Default Quotes ===
#! === 1 - Enviando n requisição por site. ===

# Nos exemplos abaixo na função start_requests foram enviados todos os link onde deve ser feito a raspagem de dados. Essa nao é a melhor abordagem uma vez que podemos não saber o numero de paginas que serão raspadas.

#? === 1° Primeira resolução ===
#* ====1.1° Scraping em 1 nivel. 
# import scrapy
# from colorama import Fore, Back, Style

# class Quotes(scrapy.Spider):
#     name = 'main' # Nome do spider
#     allowed_domains = ['quotes.toscrape.com'] # Permita acesso apenas a estes dominios.
#     start_urls = [f'https://quotes.toscrape.com/page/{url}/' for url in range(1,11)]
    
#     def parse(self, response, **kwargs):
#         blocos = response.xpath('//div[@class="quote"]')
		
#         for bloco in blocos:

#             texto = bloco.xpath('./span[@class="text"]/text()').get()
#             autor = bloco.xpath('.//small/text()').get()
#             tags = bloco.xpath('.//a[@class="tag"]/text()').getall()

#             yield {
#                 'texto' : texto,
#                 'autor' : autor,
#                 'tags' : tags 
#             }


#* ==== 1.2° Scraping em 2 nivel (duas paginas dentro do mesmo site).

# import scrapy

# class Quotes(scrapy.Spider):
#     name = 'main' # Nome do spider
#     allowed_domains = ['quotes.toscrape.com'] # Permita acesso apenas a estes dominios.
#     start_urls = [f'https://quotes.toscrape.com/page/{url}/' for url in range(1,11)]
    
#     def parse(self, response, **kwargs):
#         blocos = response.xpath('//div[@class="quote"]')
#         for bloco in blocos:
#             texto = bloco.xpath('./span[@class="text"]/text()').get()
#             autor = bloco.xpath('.//small/text()').get()
#             tags = bloco.xpath('.//a[@class="tag"]/text()').getall()
#             link = bloco.xpath('.//small[@class="author"]/../a/@href').get()
#             yield scrapy.Request(f'https://quotes.toscrape.com{link}', dont_filter = True, callback = self.parse_total, cb_kwargs = {
#                 'texto' : texto,
#                 'autor' : autor,
#                 'tags' : tags
#             })

#     def parse_total(self, response, texto, autor, tags):
#         autor_born_date = response.xpath('//span[@class="author-born-date"]/text()').get()
#         description = response.xpath('//div[@class="author-description"]/text()').get().strip()

#         yield {
#             'texto' : texto,
#             'autor' : autor,
#             'tags' : tags,
#             'autor_born_date' : autor_born_date,
#             'description' : description
#         }


#? === 2° Segunda resolução ===
#* ====2.1° Scraping em 1 nivel. 
# import scrapy

# class Quotes(scrapy.Spider):
#     name = 'main' # Nome do spider
#     allowed_domains = ['quotes.toscrape.com'] # Permita acesso apenas a estes dominios.

#     def start_requests(self):
#         for url in range(1,11,2):
#             yield scrapy.Request(f'https://quotes.toscrape.com/page/{url}/')
    
#     def parse(self, response, **kwargs):
#         blocos = response.xpath('//div[@class="quote"]')
#         for bloco in blocos:
			
#             texto = bloco.xpath('./span[@class="text"]/text()').get()
#             autor = bloco.xpath('.//small/text()').get()
#             tags = bloco.xpath('.//a[@class="tag"]/text()').getall()

#             yield {
#                 'texto' : texto,
#                 'autor' : autor,
#                 'tags' : tags 
#             }
#* ====2.2° Scraping em 2 nivel (duas paginas dentro do mesmo site).

# import scrapy

# class Quotes(scrapy.Spider):
#     name = 'main' # Nome do spider
#     allowed_domains = ['quotes.toscrape.com'] # Permita acesso apenas a estes dominios.

#     def start_requests(self):
#         for url in range(1,11):
#             yield scrapy.Request(f'https://quotes.toscrape.com/page/{url}/')
    
#     def parse(self, response, **kwargs):
#         blocos = response.xpath('//div[@class="quote"]')
#         for bloco in blocos:
#             texto = bloco.xpath('./span[@class="text"]/text()').get()
#             autor = bloco.xpath('.//small/text()').get()
#             tags = bloco.xpath('.//a[@class="tag"]/text()').getall()
#             link = bloco.xpath('.//small[@class="author"]/../a/@href').get()

#             yield scrapy.Request(f'https://quotes.toscrape.com{link}', dont_filter = True, callback = self.parse_total, cb_kwargs = {
#                 'texto' : texto,
#                 'autor' : autor,
#                 'tags' : tags
#             })

#     def parse_total(self, response, texto, autor, tags):
#         autor_born_date = response.xpath('//span[@class="author-born-date"]/text()').get()
#         description = response.xpath('//div[@class="author-description"]/text()').get().strip()

#         yield {
#             'texto' : texto,
#             'autor' : autor,
#             'tags' : tags,
#             'autor_born_date' : autor_born_date,
#             'description' : description
#         }

#? === 3° Terceira resolução ===
#* ====3.1° Scraping em 1 nivel. 
# import scrapy

# class QuoteData(scrapy.Item):
# 	quote = scrapy.Field()
# 	author = scrapy.Field()
# 	tags = scrapy.Field()

# class QuoteDataSpider(scrapy.Spider):
# 	name = "main"

# 	start_urls = [f'https://quotes.toscrape.com/page/{url}/' for url in range(1,11)]

# 	def parse(self, response):

# 		quoteData = QuoteData()
# 		quoteBlocks = response.css('div.quote')
		
# 		for block in quoteBlocks:
# 			quoteData['quote'] = block.css('span.text::text').extract_first()
# 			quoteData['author'] = block.css('span small::text').extract_first()
# 			quoteData['tags'] = block.css('div.tags a.tag::text').extract()

# 			yield quoteData	

#* ====3.2° Scraping em 2 nivel (duas paginas dentro do mesmo site).

# import scrapy

# class SeuProjetoItem(scrapy.Item):
#     texto = scrapy.Field()
#     autor = scrapy.Field()
#     tags = scrapy.Field()
#     autor_born_date = scrapy.Field()
#     description = scrapy.Field()


# class Quotes(scrapy.Spider):
#     name = 'main'  # Nome do spider

#     start_urls = [f'https://quotes.toscrape.com/page/{url}/' for url in range(1,11)]

#     def parse(self, response):
#         blocos = response.xpath('//div[@class="quote"]')
#         for bloco in blocos:
#             quoteData = SeuProjetoItem()

#             quoteData['texto'] = bloco.xpath('./span[@class="text"]/text()').get()
#             quoteData['autor'] = bloco.xpath('.//small/text()').get()
#             quoteData['tags'] = bloco.xpath('.//a[@class="tag"]/text()').getall()
#             link_about = bloco.xpath('.//small/../a/@href').get()

#             yield response.follow(link_about, dont_filter=True, callback=self.parse_total, cb_kwargs={
#                 'quoteData': quoteData
#             })

#     def parse_total(self, response, quoteData):
#         quoteData['autor_born_date'] = response.xpath('//span[@class="author-born-date"]/text()').get()
#         quoteData['description'] = response.xpath('//div[@class="author-description"]/text()').get().strip()

#         yield quoteData

#! === 2 - Enviando apenas 1 requisição por site. ===
# Nos exemplos abaixo na função start_requests foi enviado apenas o link da pagina principal os demais links foram capiturados testando se havia outra pagina.

#? === 1° Primeira resolução ===

#* ====1.1° Scraping em 1 nivel. 

# import scrapy

# class Quotes(scrapy.Spider):
#     name = 'main' # Nome do spider
#     primeira_pagina = 1

#     def start_requests(self):
#         yield scrapy.Request('https://quotes.toscrape.com/page/1/')
    
#     def parse(self, response, **kwargs):
#         blocos = response.xpath('//div[@class="quote"]')
#         for bloco in blocos:
#             texto = bloco.xpath('./span[@class="text"]/text()').get()
#             autor = bloco.xpath('.//small/text()').get()
#             tags = bloco.xpath('.//a[@class="tag"]/text()').getall()

#             yield {
#                 'texto' : texto,
#                 'autor' : autor,
#                 'tags' : tags 
#             }

#         proxima_pagina = response.xpath('//li[@class="next"]/a')
#         if proxima_pagina:
#             self.primeira_pagina += 1
#             yield scrapy.Request('https://quotes.toscrape.com/page/' + str(self.primeira_pagina), callback=self.parse)

#* ==== 1.2° Scraping em 2 nivel (duas paginas dentro do mesmo site). 

# import scrapy

# class Quotes(scrapy.Spider):
#     name = 'main' # Nome do spider
#     primeira_pagina = 1

#     def start_requests(self):
#         yield scrapy.Request('https://quotes.toscrape.com/page/1/')
    
#     def parse(self, response, **kwargs):
#         blocos = response.xpath('//div[@class="quote"]')
#         for bloco in blocos:
#             texto = bloco.xpath('./span[@class="text"]/text()').get()
#             autor = bloco.xpath('.//small/text()').get()
#             tags = bloco.xpath('.//a[@class="tag"]/text()').getall()
#             link = bloco.xpath('.//small[@class="author"]/../a/@href').get()
#             yield scrapy.Request(f'https://quotes.toscrape.com{link}', dont_filter = True, callback = self.parse_total, cb_kwargs = {
#                 'texto' : texto,
#                 'autor' : autor,
#                 'tags' : tags
#             })
            
#         proxima_pagina = response.xpath('//li[@class="next"]/a')
#         if proxima_pagina:
#             self.primeira_pagina += 1
#             yield scrapy.Request('https://quotes.toscrape.com/page/' + str(self.primeira_pagina), callback=self.parse)

#     def parse_total(self, response, texto, autor, tags):
#         autor_born_date = response.xpath('//span[@class="author-born-date"]/text()').get()
#         description = response.xpath('//div[@class="author-description"]/text()').get().strip()

#         yield {
#             'texto' : texto,
#             'autor' : autor,
#             'tags' : tags,
#             'autor_born_date' : autor_born_date,
#             'description' : description
#         }

# #? === 2° Segunda resolução ===

#* ====2.1° Scraping em 1 nivel. 

# import scrapy

# class Quotes(scrapy.Spider):
#     name = 'main' # Nome do spider

#     def start_requests(self):
#         yield scrapy.Request('https://quotes.toscrape.com/page/1/')
    
#     def parse(self, response, **kwargs):
#         blocos = response.xpath('//div[@class="quote"]')
#         for bloco in blocos:
#             texto = bloco.xpath('./span[@class="text"]/text()').get()
#             autor = bloco.xpath('.//small/text()').get()
#             tags = bloco.xpath('.//a[@class="tag"]/text()').getall()

#             yield {
#                 'texto' : texto,
#                 'autor' : autor,
#                 'tags' : tags 
#             }

#         proxima_pagina = response.xpath('//li[@class="next"]/a/@href').get()
#         if proxima_pagina:
#             yield response.follow(proxima_pagina , callback=self.parse)

#* ====2.2° Scraping em 2 nivel (duas paginas dentro do mesmo site). 

# import scrapy

# class Quotes(scrapy.Spider):
#     name = 'main' # Nome do spider

#     def start_requests(self):
#         yield scrapy.Request('https://quotes.toscrape.com/page/1/')
    
#     def parse(self, response, **kwargs):
#         blocos = response.xpath('//div[@class="quote"]')
#         for bloco in blocos:
#             texto = bloco.xpath('./span[@class="text"]/text()').get()
#             autor = bloco.xpath('.//small/text()').get()
#             tags = bloco.xpath('.//a[@class="tag"]/text()').getall()
#             link_about = bloco.xpath('.//small/../a/@href').get()
#             yield response.follow(link_about, dont_filter = True, callback = self.parse_total, cb_kwargs = {
#                 'texto' : texto,
#                 'autor' : autor,
#                 'tags' : tags
#             })
            
#         proxima_pagina = response.xpath('//li[@class="next"]/a/@href').get()
#         if proxima_pagina:
#             yield response.follow(proxima_pagina , callback=self.parse)

#     def parse_total(self, response, texto, autor, tags):
#         autor_born_date = response.xpath('//span[@class="author-born-date"]/text()').get()
#         description = response.xpath('//div[@class="author-description"]/text()').get().strip()

#         yield {
#             'texto' : texto,
#             'autor' : autor,
#             'tags' : tags,
#             'autor_born_date' : autor_born_date,
#             'description' : description
#         }

#? === 3° Terceira resolução ===

#* ====3.1° Scraping em 1 nivel. 

# import scrapy

# class SeuProjetoItem(scrapy.Item):
#     texto = scrapy.Field()
#     autor = scrapy.Field()
#     tags = scrapy.Field()

# class Quotes(scrapy.Spider):
#     name = 'main' # Nome do spider

#     def start_requests(self):
#         yield scrapy.Request('https://quotes.toscrape.com/page/1/')

#     def parse(self, response, **kwargs):
#         blocos = response.xpath('//div[@class="quote"]')
#         for bloco in blocos:
#             item = SeuProjetoItem()

#             item['texto'] = bloco.xpath('./span[@class="text"]/text()').get()
#             item['autor'] = bloco.xpath('.//small/text()').get()
#             item['tags'] = bloco.xpath('.//a[@class="tag"]/text()').getall()

#             yield item

#         proxima_pagina = response.xpath('//li[@class="next"]/a/@href').get()
#         if proxima_pagina:
#             yield response.follow(proxima_pagina , callback=self.parse)

#* ====3.2° Scraping em 2 nivel (duas paginas dentro do mesmo site). 

# import scrapy

# class SeuProjetoItem(scrapy.Item):
#     texto = scrapy.Field()
#     autor = scrapy.Field()
#     tags = scrapy.Field()
#     autor_born_date = scrapy.Field()
#     description = scrapy.Field()


# class Quotes(scrapy.Spider):
#     name = 'main'  # Nome do spider

#     def start_requests(self):
#         yield scrapy.Request('https://quotes.toscrape.com/page/1/')

#     def parse(self, response):
#         blocos = response.xpath('//div[@class="quote"]')
#         for bloco in blocos:
#             item = SeuProjetoItem()

#             item['texto'] = bloco.xpath('./span[@class="text"]/text()').get()
#             item['autor'] = bloco.xpath('.//small/text()').get()
#             item['tags'] = bloco.xpath('.//a[@class="tag"]/text()').getall()
#             link_about = bloco.xpath('.//small/../a/@href').get()

#             yield response.follow(link_about, dont_filter=True, callback=self.parse_total, cb_kwargs={
#                 'item': item
#             })

#         proxima_pagina = response.css('li.next a::attr(href)').get()
#         if proxima_pagina:
#             yield response.follow(proxima_pagina, callback=self.parse)

#     def parse_total(self, response, item):
#         item['autor_born_date'] = response.xpath('//span[@class="author-born-date"]/text()').get()
#         item['description'] = response.xpath('//div[@class="author-description"]/text()').get().strip()

#         yield item

#TODO === 3° - Site no Tableful ===

#? === 1° Primeira resolução ===

# import scrapy

# class QuoteDataSpider(scrapy.Spider):
#     name = "main"
#     primeira_pagina = 1
#     start_urls = ['http://quotes.toscrape.com/tableful/']

#     def parse(self, response):

#         quotes = response.xpath('//*[contains(@style,"border-bottom")]/*[contains(@style,"top")]/text()')
#         tags = response.xpath('//*[contains(@style,"padding-bottom")]')
        
#         for quote, tag in zip(quotes, tags):
#             text = quote.get().split(" Author: ")[0]    
#             author = quote.get().split(" Author: ")[1]
#             tags = tag.css('a::text').getall()
#             yield {
#                 'text' : text,
#                 'author' : author,
#                 'tags' : tags
#             }
            
#         proxima_pagina = response.xpath('//a[normalize-space(text()) = "Next"]')
#         if proxima_pagina:
#             self.primeira_pagina += 1
#             yield scrapy.Request('https://quotes.toscrape.com/tableful/page/' + str(self.primeira_pagina) + '/', callback=self.parse)


#? === 2° Primeira resolução ===

# import scrapy

# class QuoteData(scrapy.Item):
#     quote = scrapy.Field()
#     author = scrapy.Field()
#     tags = scrapy.Field()

# class QuoteDataSpider(scrapy.Spider):
#     name = "main"
#     primeira_pagina = 1

#     start_urls = ['http://quotes.toscrape.com/tableful/']

#     def parse(self, response):
#         quoteData = QuoteData()
#         quotes = response.xpath('//*[contains(@style,"border-bottom")]/*[contains(@style,"top")]/text()')
#         tags = response.xpath('//*[contains(@style,"padding-bottom")]')

#         for quote, tag in zip(quotes, tags):
#             quoteData['quote'] = quote.get().split(" Author: ")[0]
#             quoteData['author'] = quote.get().split(" Author: ")[1]
#             quoteData['tags'] = tag.css('a::text').getall()
#             yield quoteData

#         proxima_pagina = response.xpath('//a[normalize-space(text()) = "Next"]')
#         if proxima_pagina:
#             self.primeira_pagina += 1
#             yield scrapy.Request('https://quotes.toscrape.com/tableful/page/' + str(self.primeira_pagina), callback=self.parse)



#TODO === 4° Site login ===
# AULA 15
#? === 1° Primeira resolução ===
# No exemplo abaixo usamos não precisamos informar o token pois como a pagina tem apenas um formulario o metodo FormRequest se encarrega de pegar o token da requisição da pagina e envia junto com o 'username' e 'password'.

# import scrapy

# class LoginSpider(scrapy.Spider):
#     name = 'main'
    
#     def start_requests(self):
#         yield scrapy.FormRequest('http://quotes.toscrape.com/login', method= 'POST', formdata={
#             'username': '123',
#             'password': '123'
#         })

#     def parse(self, response, **kwargs):
#         print(response.xpath('//div[@class="col-md-4"]//a/text()').get()) # visualizando se conseguimos acessar a pagina.

#? === 2° Segunda resolução ===
# O exemplo abaixo o token não é passado de forma implicita ou seja o token não é passado de pelo metodo FormRequest.

# import scrapy
# import json

# class LoginSpider(scrapy.Spider):
#     name = 'main'
    
#     def start_requests(self):
#         yield scrapy.Request('http://quotes.toscrape.com/login')

#     def parse(self, response, **kwargs):
#         token = response.xpath('//input[@name="csrf_token"]/@value').get()
#         form_data = {
#         'csrf_token': token,
#         'username': '123',
#         'password': '123'
#         }
#         yield scrapy.FormRequest('http://quotes.toscrape.com/login', method= 'Post', formdata= form_data, callback = self.parse_login)
    
#     def parse_login(self,response):
#         print(response.xpath('//div[@class="col-md-4"]//a/text()').get())

#? === 3° Terceira resolução ===
# O exemplo abaixo é usado quando temos mais de um formulario por pagina isso significa que teremos que indicar qual formulario sera preenchido, atraves do metodo .from_response() passando o xpath do formulario (formpath = '//form').

# import scrapy
# import json

# class LoginSpider(scrapy.Spider):
#     name = 'main'
    
#     def start_requests(self):
#         yield scrapy.Request('http://quotes.toscrape.com/login')

#     def parse(self, response, **kwargs):
#         token = response.xpath('//input[@name="csrf_token"]/@value').get()
#         yield scrapy.FormRequest.from_response(response = response, callback = self.parse_login, formxpath = '//form', formdata={
#             'csrf_token': token,
#             'username': '123',
#             'password': '123'
#         })
    
#     def parse_login(self,response):
#         print(response.xpath('//div[@class="col-md-4"]//a/text()').get())

#? === 4° Quarta resolução ===

# import scrapy

# class QuoteData(scrapy.Item):
# 	quote = scrapy.Field()
# 	author = scrapy.Field()
# 	tags = scrapy.Field()

# class QuoteDataSpider(scrapy.Spider):
# 	name = "quotes"

# 	start_urls = ['http://quotes.toscrape.com/login']

# 	def parse(self, response):
# 		return scrapy.FormRequest.from_response(response, formdata={'username': 'user', 'password': 'pass'}, callback=self.after_login)
		
# 	def after_login(self, response):

# 		quoteData = QuoteData()
# 		quoteBlocks = response.css('div.quote')

# 		for block in quoteBlocks:
# 			quoteData['quote'] = block.css('span.text::text').extract_first()
# 			quoteData['author'] = block.css('span small::text').extract_first()
# 			quoteData['tags'] = block.css('div.tags a.tag::text').extract()

# 			yield quoteData	

# 		# follow pagination links
# 		for a in response.css('li.next a'):
# 			yield response.follow(a, callback=self.after_login)

#TODO === 5° - Requisições com paginas em scroll infinito === 
#? === 1° Primeira resolução ===
# AULA 21
# import scrapy 

# class QuotesXHR(scrapy.Spider):
#     name = 'main'

#     def start_requests(self):
#         yield scrapy.Request('http://quotes.toscrape.com/api/quotes?page=1')

#     def parse(self, response, **kwargs):
#         dicionario = response.json()
        
#         quotes = dicionario.get('quotes')
#         for quote in quotes:
#             author_name = quote.get('author').get('name')
#             # tags = quote.get('tags') # Pegar no formato de lista.
#             tags = ';'.join(quote.get('tags')) # Pegar no formato de string.
#             text = quote.get('text')
#             yield{
#                 'author_name' : author_name,
#                 'tags' : tags,
#                 'text' : text
#             }
        
#         has_next_page = dicionario.get('has_next')
#         next_page = dicionario.get('page') + 1 
#         if has_next_page:
#             yield scrapy.Request(f'http://quotes.toscrape.com/api/quotes?page={next_page}', callback=self.parse)

#? === 2° Segunda resolução ===
# import scrapy

# class QuoteData(scrapy.Item):
#     author_name = scrapy.Field()
#     tags = scrapy.Field()
#     text = scrapy.Field()

# class QuotesXHRSpyder(scrapy.Spider):
#     name = 'main'

#     def start_requests(self):
#         yield scrapy.Request('http://quotes.toscrape.com/api/quotes?page=1')

#     def parse(self, response, **kwargs):

#         data_dict = response.json()
#         quotes = data_dict.get('quotes')
#         quote_data = QuoteData()

#         for quote in quotes:
#             quote_data['author_name'] = quote.get('author').get('name')
#             quote_data['tags'] = ';'.join(quote.get('tags'))
#             quote_data['text'] = quote.get('text')

#             yield quote_data

#         has_next_page = data_dict.get('has_next')
#         next_page = data_dict.get('page') + 1
#         if has_next_page:
#             yield scrapy.Request(f'http://quotes.toscrape.com/api/quotes?page={next_page}', callback=self.parse)


#TODO === 6° - Conteúdo gerado por JavaScript ===
# AULA 23
#! === 1 - Usando a biblioteca chompjs. ===
#? === 1° Primeira resolução ===
# import scrapy
# import chompjs


# class QuotesJavascripts(scrapy.Spider):
#     name = 'main'

#     def start_requests(self):
#         yield scrapy.Request('http://quotes.toscrape.com/js/')

#     def parse(self, response, **kwargs):
#         list_of_dicts = chompjs.parse_js_object(response.xpath('//script[contains(text(), "var data")]//text()').get())
#         for item in list_of_dicts:
            
#             tags = ';'.join(item.get('tags'))
#             author_name = item.get('author').get('name')
#             text = item.get('text')
            
#             yield {
#                 'author_name' : author_name,
#                 'tags' : tags,
#                 'text' : text
#             }
#         next_page = response.xpath('//li[@class="next"]/a/@href').get()
#         if next_page:
#             yield response.follow(next_page, callback=self.parse)

#? === 2° Primeira resolução ===
# import scrapy
# import chompjs

# class QuoteData(scrapy.Item):
#     author_name = scrapy.Field()
#     tags = scrapy.Field()
#     text = scrapy.Field()

# class QuotesJavascriptsSpider(scrapy.Spider):
#     name = 'main'

#     start_urls = ['http://quotes.toscrape.com/js/']

#     def parse(self, response):
#         script_text = response.xpath('//script[contains(text(), "var data")]//text()').get()
#         list_of_dicts = chompjs.parse_js_object(script_text)
#         quote_data = QuoteData()

#         for item in list_of_dicts:
#             quote_data['tags'] = ';'.join(item.get('tags'))
#             quote_data['author_name'] = item.get('author').get('name')
#             quote_data['text'] = item.get('text')

#             yield quote_data

#         next_page = response.xpath('//li[@class="next"]/a/@href').get()
#         if next_page:
#             yield response.follow(next_page, callback=self.parse)


#! === 2 - Usando a biblioteca json. ===
#? === 1° Primeira resolução ===
#versão simplificada
# https://www.youtube.com/watch?v=dKAKVVciU5M&t=816s

#? === 2° Segunda resolução ===
import scrapy
import json
import re
from scrapy_splash import SplashRequest

class QuoteData(scrapy.Item):
	quote = scrapy.Field()
	author = scrapy.Field()
	tags = scrapy.Field()

class QuoteDataSpider(scrapy.Spider):
	name = "main"

	start_urls = ['http://quotes.toscrape.com/js/page/1/']

	def start_requests(self):
		for url in self.start_urls:
			yield SplashRequest(url, self.parse, endpoint='render.html',args={'wait': 0.5},)

	def parse(self, response):

		quoteData = QuoteData()
		data = re.findall("var data =(.+?);\n", response.body.decode("utf-8"), re.S)

		dataJSON = []
		if data:
			dataJSON = json.loads(data[0])

		for item in dataJSON:
			quoteData['quote'] = item.get('text')
			quoteData['author'] = item.get('author', {}).get('name')
			quoteData['tags'] = item.get('tags')

			yield quoteData

		# follow pagination links
		for a in response.css('li.next a'):
			yield response.follow(a, callback=self.parse)

#TODO === 7° - Conteúdo gerado por JavaScript com Delayed ===
# AULA 24
#? === 1° Primeira resolução ===

# import scrapy
# import chompjs

# class QuotesJavascripts(scrapy.Spider):
#     name = 'main'

#     def start_requests(self):
#         yield scrapy.Request('http://quotes.toscrape.com/js-delayed/')

#     def parse(self, response, **kwargs):
#         text = response.xpath("//script[contains(text(), 'var data')]//text()").get()
#         dicionario = chompjs.parse_js_object(text[text.index('var data') : ])

#         for item in dicionario:
            
#             tags = ';'.join(item.get('tags'))
#             author_name = item.get('author').get('name')
#             text = item.get('text')
            
#             yield {
#                 'author_name' : author_name,
#                 'tags' : tags,
#                 'text' : text
#             }
        
#         next_page = response.xpath('//li[@class="next"]/a/@href').get()
#         if next_page:
#             yield response.follow(next_page, callback=self.parse)

#? === 2° Segunda resolução ===

# import scrapy
# import chompjs

# class QuoteData(scrapy.Item):
#     author_name = scrapy.Field()
#     tags = scrapy.Field()
#     text = scrapy.Field()

# class QuotesJavascriptsSpider(scrapy.Spider):
#     name = 'main'

#     def start_requests(self):
#         yield scrapy.Request('http://quotes.toscrape.com/js-delayed/')

#     def parse(self, response, **kwargs):
#         text = response.xpath("//script[contains(text(), 'var data')]//text()").get()
#         data_dict = chompjs.parse_js_object(text[text.index('var data'):])
#         quote_data = QuoteData()

#         for item in data_dict:
#             quote_data['tags'] = ';'.join(item.get('tags'))
#             quote_data['author_name'] = item.get('author').get('name')
#             quote_data['text'] = item.get('text')

#             yield quote_data
        
#         next_page = response.xpath('//li[@class="next"]/a/@href').get()
#         if next_page:
#             yield response.follow(next_page, callback=self.parse)


#TODO === 8° - Com um formulário de filtro baseado em AJAX com ViewStates ===
# AULA 25 - 26

#? === 1° Primeira resolução ===

# import scrapy
# import chompjs

# class AspxSpider(scrapy.Spider):
#     name = 'main'

#     def start_requests(self):
#         yield scrapy.Request('http://quotes.toscrape.com/search.aspx')

#     def parse(self, response, **kwargs):
#         token = response.xpath("//input[@id='__VIEWSTATE']/@value").get()
#         authors = response.xpath("//select[@id='author']//option/@value").getall()
#         for author in authors:
#             yield scrapy.FormRequest('http://quotes.toscrape.com/filter.aspx', formdata={
#                 'author' : author,
#                 '__VIEWSTATE' : token
#             }, callback = self.parse2, cb_kwargs = {'author': author})

#     def parse2(self, response, author):
#         token = response.xpath("//input[@id='__VIEWSTATE']/@value").get()
#         tags = response.xpath("//select[@id='tag']//option/@value").getall()
#         for tag in tags:
#             yield scrapy.FormRequest('http://quotes.toscrape.com/filter.aspx', formdata = {
#                 'author' : author,
#                 'tag' : tag,
#                 'submit_button' : 'Search',
#                 '__VIEWSTATE' : token
#             }, callback = self.parse_quotes, cb_kwargs={
#                 'author' :author,
#                 'tag' : tag
#                 })

#     def parse_quotes(self,response, author, tag):
#         quotes = response.xpath('//div[@class="quote"]')
#         for quote in quotes:
#             text = quote.xpath('.//span[@class="content"]//text()').get()
#             yield {
#                 'text' : text,
#                 'author' : author,
#                 'tag' : tag
#             }


#? === 2° Segunda resolução ===

# import scrapy

# class QuoteData(scrapy.Item):
# 	quote = scrapy.Field()
# 	author = scrapy.Field()
# 	tags = scrapy.Field()

# class QuoteDataSpider(scrapy.Spider):
# 	name = "quotes"

# 	start_urls = ['http://quotes.toscrape.com/search.aspx']

# 	def parse(self, response):
# 		for author in response.css('select#author > option::attr(value)').extract():
# 			yield scrapy.FormRequest('http://quotes.toscrape.com/filter.aspx', formdata = {'author':author, '__VIEWSTATE': response.css('input#__VIEWSTATE::attr(value)').extract_first()}, callback=self.parse_tags)

# 	def parse_tags(self, response):
# 		for tag in response.css('select#tag > option::attr(value)').extract():
# 			yield scrapy.FormRequest('http://quotes.toscrape.com/filter.aspx', formdata={'author': response.css('select#author > option[selected]::attr(value)').extract_first(), 'tag':tag, '__VIEWSTATE': response.css('input#__VIEWSTATE::attr(value)').extract_first()},callback=self.parse_results)

# 	def parse_results(self, response):
# 		quoteData = QuoteData()
# 		for quote in response.css('div.quote'):
# 			quoteData['quote'] = quote.css('span.content::text').extract_first()
# 			quoteData['author'] = quote.css('span.author::text').extract_first()
# 			quoteData['tags'] = quote.css('span.tag::text').extract_first()
# 			yield quoteData

