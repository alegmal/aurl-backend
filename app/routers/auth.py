from fastapi import APIRouter
from pydantic import BaseModel
from typing import Union

router = APIRouter()

# class Item(BaseModel):
#     name: str
#     price: float
#     is_offer: Union[bool, None] = None

router = APIRouter()

@router.get("/login")
async def login():
    return {"login page"}

@router.get("/register")
async def register():
    return {"register page"}