from fastapi import FastAPI

from .routers import auth

app = FastAPI()
app.include_router(auth.router)

@app.get("/")
async def read_root():
    return {"front page"}


