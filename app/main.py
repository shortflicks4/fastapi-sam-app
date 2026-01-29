from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()

@app.get("/health")
def health():
    return {"stats": "ok4"}

handler = Mangum(app)
