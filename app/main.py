from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok3"}

handler = Mangum(app)
