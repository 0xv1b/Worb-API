from lib2to3.pgen2.token import OP
from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import redis

class Word(BaseModel):
    text: str
    frequency: Optional[int] = 0

app = FastAPI()
r = redis.Redis()

@app.get("/word/{word}")
def get_word(word: str):
    if (r.exists(word)):
        return Word(text = word, frequency = r.get(word)).json()
    else:
        return Word(text = word).json()

@app.post("/word/")
def post_word(word: Word):
    if (r.exists(word.text)):
        r.incr(word.text)
    else:
        r.set(word.text, 1)

