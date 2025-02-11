from flask import   Flask, request
from db import stores, items
import uuid

app = Flask(__name__)



@app.get("/store") #http://127.0.0.1:5000/store
def get_stores():
    return {"stores": list(stores.values())},200


@app.get("/store/<string:store_id>")
def get_specific_store(store_id):
    if store_id in stores:
        return {"store": stores[store_id]}, 200
    else:
        return {"message": "Store not found"}, 404


@app.get("/item/<string:item_id>")
def get_item(item_id):
    if item_id in items:
        return {"item": items[item_id]}, 200
    else:
        return {"message": "Item not found"}, 404
                

@app.post("/store")
def create_store():
    store_data = request.get_json()
    store_id = uuid.uuid4().hex
    store = {**store_data,"store_id":store_id}
    stores[store_id] = store
    return store, 201




@app.post("/item")
def create_item():
    #informacion que manda incide 
    item_data = request.get_json()
    if item_data['store_id'] not in stores:
        return {"message": "Store not found"}, 404
    else:
        item_id = uuid.uuid4().hex
        item = {**item_data,"item_id": item_id}
        items[item_id] = item
        return item, 201