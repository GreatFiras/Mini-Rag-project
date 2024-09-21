from pydantic import BaseModel
from typing import Optional
class ProcessRequest(BaseModel): #you will rrecivce a request with a file :str , id 
    file_id : str 
    chunk_size: Optional[int] = 100  
    overlap_size: Optional[int] =  20
    do_reset : Optional[int] = 0 #adding prefix do_ = the parameter will do an action   
