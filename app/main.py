from fastapi import FastAPI, Request

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)

@app.get("/")
def read_root():
    with get_conn() as conn, conn.cursor() as cur:
        cur.execute("SELECT 'hello postgres' ")
    return {"msg" : "Hotel APLI!"}

@app.get("/api/ip")
def read_root(request : Request):
    return {"client_ip": request.client.host}

rooms = [
    {"room_number": 101, "price": 90},
    {"room_number": 102, "price": 110},
    {"room_number": 201, "price": 230}
]

@app.get("/rooms")
def get_rooms():
    return rooms