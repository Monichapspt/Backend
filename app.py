from logging import error
from flask import Flask, request
from flask_restful import Resource, Api, reqparse
import json

app = Flask(__name__)
api = Api(app)

null = None

class home(Resource):
    def get(self):
        f = open("home.json","r")
        data = json.load(f)
        return data

class about(Resource):
    def get(self):
        f = open("about.json","r")
        data = json.load(f)
        return data

class practice(Resource):
    def get(self):
        f = open("practice.json","r")
        data = json.load(f)
        return data

class blog(Resource):
    def get(self):
        f = open("blog.json","r")
        data = json.load(f)
        return data

class elements(Resource):
    def get(self):
        f = open("elements.json","r")
        data = json.load(f)
        return data

class contact(Resource):
    def get(self):
        f = open("contact.json","r")
        data = json.load(f)
        return data

api.add_resource(home, '/home/')
api.add_resource(about,'/about/')
api.add_resource(practice,'/practice/')
api.add_resource(blog,'/blog/')
api.add_resource(elements,'/elements/')
api.add_resource(contact,'/contact/')

@app.errorhandler(404)
def page_not_found(e):
    return {"error":"Gak enek file e"}, 404

if __name__ == '__main__':
    app.run(debug=True,port=5005)