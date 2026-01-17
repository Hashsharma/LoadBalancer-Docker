from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def greetings():
    return {"result": "Greetings to all"}

