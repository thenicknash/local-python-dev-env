from typing import Union

from fastapi import FastAPI

import redis

app = FastAPI()

r = redis.Redis(host="redis", port=6379)


@app.get("/")
def read_root():
    return {"Hello": "World", "this is": "a test"}


@app.get("/hits")
def read_root():
    r.incr("hits")
    return {"number of hits": r.get("hits")}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}