from pydantic import BaseModel
from datetime import datetime

class PostBase(BaseModel):
  image_url: str
  title: str
  content: str
  creator: str
  
class PostDisplay(BaseModel):
  id: int
  image_url: str
  title: str
  content: str
  creator: str
  timestamp: datetime
  #this map what in the database to this class
  class Config():
    orm_mode = True