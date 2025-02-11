from flask import   Flask, request,abort
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
        return abort(404, message= f"Store not found")


@app.get("/item/<string:item_id>")
def get_item(item_id):
    if item_id in items:
        return {"item": items[item_id]}, 200
    else:
        return abort(404, message= f"Item not found")
                

@app.post("/store")
def create_store():
    store_data = request.get_json()
    if 'name' not in store_data:
        abort(404, message= f"Name is required")
    
    for store in stores.values():
        if store['name'] == store_data['name']:
            abort(404, message= f"Store with the same name already exists")
    store_id = uuid.uuid4().hex
    store = {**store_data,"store_id":store_id}
    stores[store_id] = store
    return store, 201


@app.post("/item")
def create_item():
    #informacion que manda incide 
    item_data = request.get_json()
    if ('store_id' not in item_data or 
        'name' not in item_data or 
        'price' not in item_data):
        abort(404, message= f"Store not found")
    else:
        item_id = uuid.uuid4().hex
        item = {**item_data,"item_id": item_id}
        items[item_id] = item
        return item, 201
    

@app.delete("/item/<item_id>")
def delete_item(item_id):
    if item_id in items:
        del items[item_id]
        return {"message": "Item deleted successfully"}, 200
    else:
        return abort(404, message= f"Item not found")
    

@app.delete("/store/<store_id>")
def delete_store(store_id):
    if store_id in stores:
        del stores[store_id]
        return {"message": "Store deleted successfully"}, 200
    else:
        return abort(404, message= f"Store not found")


@app.put("/item/<item_id>")
def update_item(item_id):
    item_data = request.get_json()
    if item_id in items:
        items[item_id].update(item_data)
        return {"item": items[item_id]}, 200
    else:
        return abort(404, message= f"Item not found")
