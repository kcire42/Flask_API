from flask import   Flask, request

app = Flask(__name__)

stores = [
    {"name": "My_Store",
      "items": [
          {"name": "Item 1", "price": 10.99},
          {"name": "Item 2", "price": 8.99}]},
    {"name": "Your Store", 
     "items": [
         {"name": "Item 2", "price": 15.99},
         {"name": "Item 3", "price": 12.99}]},
    {"name": "those Store", 
     "items": [
         {"name": "Item 4", "price": 16.43},
         {"name": "Item 5", "price": 32.34}]},      
]

@app.get("/store") #http://127.0.0.1:5000/store
def get_stores():
    return {"stores": stores},200

@app.post("/store")
def create_store():
    request_data = request.get_json()
    new_store = {"name": request_data["name"], "items": []}
    stores.append(new_store)
    return new_store,201


@app.post("/store/<string:name>/item")
def create_item(name):
    #informacion que manda incide 
    request_data = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {'name':request_data['name'],'price':request_data['price']}
            store['items'].append(new_item)
            return new_item, 201
    return {"message": "Store not found"}, 404


@app.get("/store/<string:name>")
def get_specific_store(name):
    for store in stores:
        if store['name'] == name:
            return {'store': store['items']},200
    return {"message": "Store not found"}, 404


@app.get("/store/<string:name>/<string:item>")
def get_item(name, item):
    for store in stores:
        if store['name'] == name:
            for i in store['items']:
                if i['name'] == item:
                    return {'item': i}, 200