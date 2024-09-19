from fastapi import FastAPI
from routes import base

app = FastAPI(
    prefix = '/api/v1' , tags = ['api_v1']
)

@app.include_routes(base.base_router)
def welcome():
    return {
        "message": "Hello World!"
    }