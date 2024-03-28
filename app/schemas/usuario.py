import re
from pydantic import validator, EmailStr, BaseModel
from datetime import datetime


class Usuarios(BaseModel):
    username: str
    password: str
    email: EmailStr

    @validator('username')
    def validate_username(cls, value):
        if not re.match('^([a-z]|[A-Z]|[0-9]|-|_|@)+$', value):
            raise ValueError('Invalid username')
        return value

class UsuarioRequest(Usuarios):
    username: str
    email: EmailStr
    password: str

class UsuarioResponse(Usuarios):
    id: int
    username: str
    email: str
    password: str


    class Config:
        from_attributes=True    
        orm_mode = True