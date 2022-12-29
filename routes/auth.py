from fastapi import APIRouter, Header
from pydantic import BaseModel, EmailStr
from funtions_jwt import write_token, validate_token
from fastapi.responses import JSONResponse
from schemas.user import User
from models.user import users
from conf.db import con

auth_routes = APIRouter() 


@auth_routes.post("/login/token", tags=["Usuarios"])
def login(user: User):
    print(user.dict())
    result = con.execute(users.select().where(users.c.username == user.username and users.c.password == user.password)).first()
    print(result)
    if result:
        return write_token(user.dict())
    else:
        return JSONResponse(content={"message": "User not found"}, status_code=200)
    

@auth_routes.get("/verify/token", tags=["Usuarios"])
def verify_token(Authorization: str = Header(None)):
    token = Authorization.split(" ")[1]
    return validate_token(token, output=True)