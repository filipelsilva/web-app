import pymongo
import db
from flask import Flask, jsonify, request

client = None
database = None
user = None
table = None
app = Flask("backend")

@app.route('/get-notes', methods = ['GET'])
def get_notes():
    return db.get_notes(table)

@app.route('/add-note', methods = ['POST'])
def add_note():
    content = request.get_json()
    print(request.args.get('content'))
    return {}
    # return db.add_note(table, user, content)

@app.route('/remove-note', methods = ['POST'])
def remove_note():
    # content = request.get_json()
    # print(request.args.get('content'))
    return {}
    # return db.remove-note(table, id)

@app.route('/edit-note/<int:id>/', methods = ['POST'])
def edit_note(id):
    # content = request.get_json()
    # print(request.args.get('content'))
    return {}
    # db.edit_note(table, id, content)

if __name__ == "__main__":
    client = db.get_client(
        "mongodb://%s:%s@localhost:27017",
        "admin",
        "password",
    )
    database = db.get_database(
        client,
        "notes",
    )
    user = "user1"
    table = db.get_table(database, user) # TODO add users
    app.run(debug = True)
