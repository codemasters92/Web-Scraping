# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


#? === Pipeline original do scrapy
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
class BooksPipeline:
    def process_item(self, item, spider):
        return item

#? === Pipeline criada para salvar as imagens com o nome
# from scrapy.pipelines.images import ImagesPipeline
# class BooksPipeline(ImagesPipeline):

#     def file_path(self, request, response = None, info = None, *, item = None):
#         image_guide = item['url'].split('/')[-2]
#         return f'full2/{image_guide}.jpg'


#? === Pipeline criada para salvar os dados em um banco de dados.
#aula 37 38 39
# import sqlite3
# class SqlitePipeline():
    
#     db = sqlite3.connect('books.db')
#     cur = db.cursor()

#     cur.execute('''CREATE TABLE IF NOT EXISTS books(
#             title Text, 
#             price Text, 
#             stock Text, 
#             rating Text, 
#             url Text, 
#             image_urls Text, 
#             upc Text, 
#             reviews Text, 
#             tag Text 
#     )''')

#     def open_spider(self, spider):
#         spider.logger.info("Aranha iniciada.")

#     def process_item(self, item, spider):
#         try:
#             self.cur.execute('''
#                 INSERT INTO books (title, price, stock, rating, url, image_urls, upc, reviews, tag)
#                 VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
#             ''', (
#                 item['title'],
#                 item['price'],
#                 item['stock'],
#                 item['rating'],
#                 item['url'],
#                 ''.join(item['image_urls']),
#                 item['upc'],
#                 item['reviews'],
#                 item['tag']
#             ))
#             # Commit a transação para salvar os dados no banco de dados
#             self.db.commit()
#             spider.logger.info(f"Dados inseridos com sucesso")
#             return item
#         except sqlite3.Error as e:
#             # Se ocorrer um erro ao inserir dados, você pode lidar com ele aqui
#             spider.logger.error(f"Erro ao inserir dados no banco de dados: {str(e)}")
#             return None

#     def close_spider(self, spider):
#         self.db.close()
#         spider.logger.info("Aranha encerrada.")



#? === Pipeline criada para salvar os dados em um banco de dados com ORM peewee.
#Aula 40 E 41. 
from peewee import SqliteDatabase, TextField, Model

class SqlitePipeline():
    def __init__(self):
        self.db = SqliteDatabase('books2.db')
        self.db.connect()
        self.create_table()

    def create_table(self):
        self.db.create_tables([BooksModel], safe=True)

    def open_spider(self, spider): # Metodo desnecessario para funcionamento desse metodo devemos mudar o middkewares.py
        spider.logger.info("Aranha iniciada.")

    def process_item(self, item, spider):
        try:
            it = BooksModel(**item)
            it.save()
            spider.logger.info("Dados inseridos com sucesso")
            return item
        except Exception as e:
            # Se ocorrer um erro ao inserir dados, você pode lidar com ele aqui
            spider.logger.error(f"Erro ao inserir dados no banco de dados: {str(e)}")
            return None

    def close_spider(self, spider): # Metodo desnecessario para funcionamento desse metodo devemos mudar o middkewares.py
        spider.logger.info("Aranha encerrada.")

class BooksModel(Model):
    title = TextField(null=True)
    price = TextField(null=True)
    stock = TextField(null=True)
    rating = TextField(null=True)
    url = TextField(null=True)
    image_urls = TextField(null=True)
    upc = TextField(null=True)
    reviews = TextField(null=True)
    tag = TextField(null=True)

    class Meta:
        database = SqliteDatabase('books2.db')


#? === Pipeline criada para salvar os dados em um banco de dados com MongoDB.








