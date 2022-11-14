from fastapi import FastAPI, APIRouter

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}