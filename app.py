import json
from os import abort
from re import L, split
from bson import json_util
from bson.objectid import ObjectId
import datetime
from flask.app import Flask
from flask.json import jsonify
from flask.wrappers import Request, Response
import pymongo
from pymongo import MongoClient
from pymongo.message import update
from werkzeug.wrappers import request, response

from flask import Flask
from flask import request
from pymongo import MongoClient
from bson.json_util import dumps

cluster = MongoClient("mongodb+srv://aliboran:054zkwaW2ehsfZZN@cluster0.crffc.mongodb.net/Story?retryWrites=true&w=majority")
db=cluster['User_Story']
collection=db['todos']

print(db.collection_names())

app=Flask(__name__)


@app.route('/story/',methods=['GET'])
def get_story():
    story = collection.find()
    response=json_util.dumps(story)
    return Response(response,mimetype="application/json")

@app.route('/story/add/',methods=['POST'])
def create_story():
    #data=request.get_json()
    _json = request.get_json()
    title= _json["title"]
    description=_json["description"]
    is_completed=_json
    created_at=_json[datetime.datetime.now()]
    updated_at=_json[datetime.datetime.now()]
    #data = json.loads(request.data)
    story={
        "title":title["title"],
        "description":description["description"],
        "is_completed":is_completed[False],
        "created_at":created_at[datetime.datetime.now()],
        "updated_at":updated_at[datetime.datetime.now()]
    }
    print(story)
    res=collection.insert_one(story)
    
    return jsonify({"message":f"user added on ${res}"})

@app.route('/update',methods=['PUT'])
def update_story():
    _json =request.json
    id= _json["title"]
    title= _json["title"]
    description=_json["description"]
    is_completed=_json[True]
    created_at=_json[datetime.datetime.now()]
    updated_at=_json[datetime.datetime.now()]

    if title and description and is_completed and created_at and updated_at and request.method=='POST':
        id=collection.update_one({"_id":ObjectId(id['$oid']),"title":title, "description":description,"is_completed":False, "created_at":datetime.datetime.now(), "updated_at":datetime.now()})
        resp=jsonify("User added successfully")
        resp.status_code=200
        return resp
    else:
        return not_found() 

@app.route('/story/<id>',methods=['DELETE'])
def delete_story(id):
      delete_s=collection.delete_one({"_id":ObjectId(id)})
      resp=jsonify("User deleted successfully ",delete_s)
      resp.status_code=200
      return resp


@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404    

if __name__== '__main__':
    app.run(debug=True)