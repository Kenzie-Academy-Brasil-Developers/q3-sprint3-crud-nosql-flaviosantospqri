from datetime import datetime
from flask import request
import pymongo


client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["kenzie"]

class Post:
    def __init__(self,id,title, author, tags:list, content):
        self.id = id
        self.created_at = datetime.now()
        self.update_at = datetime.now()
        self.title = title
        self.author = author
        self.tags = tags
        self.content = content
    
    @staticmethod
    def get_all():
        list_post = db.posts.find()
        return list_post
    
    def post_posts(self):
       return db.posts.insert_one(self.__dict__)
    
    def generate_date(post):
        return post._id.generation_time
        

    @staticmethod
    def del_post(id):
       current_delete =  db.posts.find_one_and_delete({"id":id})
       return current_delete

    @staticmethod
    def get_one(id):
       current_one =  db.posts.find_one({"id":id})
       return current_one

    @staticmethod
    def get_update(self, id):
        new_information = request.get_json() 
        return db.posts.find_one_and_update({"id":id}, {"$set": new_information},  return_document=True)
    