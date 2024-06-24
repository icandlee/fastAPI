from fastapi import FastAPI
from enum import Enum

class LoginMethod(str, Enum):
    google = "google"
    kakao = "kakao"
    namver = "naver"
    apple = "apple"


app = FastAPI()


@app.get("/")
def root():
    return {"message":"test"}


@app.get("/home/{name}")
def home(name:LoginMethod): 
    return {"message":name}
 