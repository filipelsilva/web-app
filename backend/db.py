from datetime import datetime
import json, pymongo

def get_timestamp_now():
    return str(int(datetime.utcnow().timestamp()))

def get_client(url, username, password):
    try:
        return pymongo.MongoClient(url % (username, password))
    except pymongo.errors.ConnectionFailure as e:
        print(f"Could not connect to server: {e}")
        exit(1)

def get_database(client, database_name):
    return client[database_name]

def get_table(database, user):
    return database[user]

def get_notes(table):
    return list(table.find())

def add_note(table, user, content):
    len = table.count_documents({})
    now = get_timestamp_now()
    note = {
        "_id": now,
        "last-modified": now,
        "note": content
    }
    table.insert_one(note)

def remove_note(table, id):
    query = {
        "_id": id
    }
    table.delete_one(query)

def edit_note(table, id, content):
    query = {
        "_id": id
    }
    new_values = {
        "$set": {
            "last-modified": get_timestamp_now(),
            "note": content
        }
    }
    table.update_one(query, new_values)
