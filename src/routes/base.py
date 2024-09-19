from fastapi import FastAPI , APIRouter
import os 

base_router = APIRouter()

@base_router.get("/")
def welcome():
    
    app_name = os.getenv('APP_NAME')
    app_version = os.getenv('APP_VERSION')
    # OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

    return {
        
        "app_name": app_name , 
        'app_version' : app_version , 
    }
