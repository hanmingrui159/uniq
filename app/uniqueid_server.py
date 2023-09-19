import os
from datetime import datetime, time, timedelta
import random
import pickle

from typing import Optional
from fastapi import FastAPI, Response, Body
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

import json
from uniqueid import *
app = FastAPI()
s = snowid_generator(3,7)

@app.get("/")
async def root():
    return "go /docs for API details"

@app.get("/uuid4")
async def request_uuid4():
    i = get_uuid4_hex()
    # print(i)
    return i

@app.get("/snowid")
async def request_snowid():
    i = next(s)
    # print(i)
    return i

# if __name__ == '__main__':
#     main()
    