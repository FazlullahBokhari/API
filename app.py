from flask import Flask 


app = Flask(__name__)


stores = [
        {
            "name": "My Store",
            "items": [
                {
                    "name": "Chair",
                    "price": 175.50
                }
            ]
        }]

@app.get("/store")
def get_store():
    return {"Store ": stores} 


@app.post("/store")
def create_store():
    pass

