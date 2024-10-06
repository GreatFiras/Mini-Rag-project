from pydantic import BaseModel , Field
from typing import Optional
from bson.objectid import ObjectId


class Project(BaseModel): 
    
    #objectid is the type of how the mongodb consider the id string in the database; 
    id: Optional[ObjectId] = Field(None , alias='_id')
    project_id : str = Field(... , min_length=1)


# we use manual validator because "pydantic" is not familiar with type "ObjectId", and we need to do config class 
    @validator('project_id')  
    def validate_project_id (cls, value ):  #cls represent the class Project itself; 

        if not value.isalnum(): 
            raise ValueError("Value Must BE ALPHA NUMERIC")
        
        return value 
    

    class Config: 
        arbitrary_types_allowed = True
    
