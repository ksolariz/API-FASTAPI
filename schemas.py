from pydantic import BaseModel

class UserCreateInput(BaseModel):
    name: str

class Default_message(BaseModel):
    message: str
