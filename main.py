from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Git FastAPI Practice"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/users")
def get_users():
    return {
        "users": [
            {"id": 1, "name": "감자"},
            {"id": 2, "name": "FastAPI"}
        ]
    }
