from fastapi import FastAPI
import uvicorn
import os

app = FastAPI()

@app.get("/")
def hello():
    return {"message": "Hello from FastAPI on Cloud Run via GitHub!"}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    uvicorn.run("main:app", host="0.0.0.0", port=port)
