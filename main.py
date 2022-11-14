from fastapi import FastAPI, APIRouter

from views.views import user_router

app = FastAPI()
router = APIRouter()

@app.get("/")
async def read_root():
    return {"Hello": "World"}

app.include_router(user_router)