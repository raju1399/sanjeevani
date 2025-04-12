from fastapi import FastAPI
from app.routes import scan

app = FastAPI(title="Sanjeevani - Cybersecurity Platform")

app.include_router(scan.router)

@app.get("/")
def read_root():
    return {"message": "Sanjeevani API is live!"}
