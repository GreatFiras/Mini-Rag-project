from fastapi import FastAPI
from dotenv import load_dotenv
load_dotenv('.env')

from routes import base
app = FastAPI(
    # prefix = '/api/v1' , tags = ['api_v1']
)

@app.include_routes(base.base_router)
def welcome():
    return {
        "message": "Hello World!"
    }