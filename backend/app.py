import pymongo
import db
from flask import Flask, jsonify, request
from flask_cors import CORS

client = None
database = None
user = None
table = None
app = Flask("backend")
CORS(app)

@app.route('/get-notes', methods = ['GET'])
def get_notes():
    return jsonify(db.get_notes(table))

@app.route('/add-note', methods = ['POST'])
def add_note():
    content = request.get_json()['content']
    db.add_note(table, user, content)
    return "Added note"

@app.route('/remove-note/<id>', methods = ['GET'])
def remove_note(id):
    db.remove_note(table, id)
    return "Removed note"

@app.route('/edit-note/<id>', methods = ['POST'])
def edit_note(id):
    req = request.get_json()
    content = req['content']
    db.edit_note(table, id, content)
    return "Edited note"

if __name__ == "__main__":
    client = db.get_client(
        "mongodb://%s:%s@database:27017",
        "admin",
        "password",
    )
    database = db.get_database(
        client,
        "notes",
    )
    user = "user1"
    table = db.get_table(database, user) # TODO add users
    app.run(
        host = "0.0.0.0",
        port = 5000,
        debug = True
    )
