import pymongo, datetime

CONNECTION_STRING = "mongodb://%s:%s@localhost:27017"

database = None
table = None
user = None

def get_database(url, database_name, username, password):
    client = pymongo.MongoClient(url % (username, password))
    return client[database_name]

def get_table(database, user):
    return database[user]

def print_table(table):
    for el in table.find({}):
        print(el)

def add_note(table, user, content):
    len = table.count_documents({})
    note = {
        "date": datetime.datetime.today(),
        "user": user,
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
            "date": datetime.datetime.today(),
            "note": content
        }
    }
    table.update_one(query, new_values)

if __name__ == "__main__":
    database = get_database(CONNECTION_STRING, "notes", "admin", "password")
    user = "user1"
    table = get_table(database, user) # TODO add users
    # add_note(table, user, "teste")
