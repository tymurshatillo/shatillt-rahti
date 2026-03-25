from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/api/ip")
def read_root(request : Request):
    return {"client_ip": request.client.host}

@app.get("/items/{id}")
def read_item(item_id: int, q: str = None):
    return {"id": id, "q": q}   
