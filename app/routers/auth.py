from fastapi import APIRouter, Depends, Security
from fastapi.security import HTTPBearer
from ..utils.auth0_jwt import VerifyToken

router = APIRouter()
auth = VerifyToken()
# token_auth_scheme = HTTPBearer()

# async def private(token: str = Depends(token_auth_scheme)):
@router.get("/login")
async def private(auth_result: str = Security(auth.verify)):
    return auth_result

@router.get("/register")
async def register():
    return {"register page"}