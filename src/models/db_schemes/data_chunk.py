from pydantic import BaseModel , Field , validator 
from typing import Optional
from bson.objectid  import ObjectId

class DataChunk(BaseModel): 

    _id: Optional[ObjectId]
    chunk_text: str = Field(... , min_length=1)
    chunk_meta_data: dict 
    chunk_order: int = Field(... , gt = 0 ) # greater than; 
    chunk_project_id: ObjectId




    class Config: 
        arbitrary_types_allowed = True