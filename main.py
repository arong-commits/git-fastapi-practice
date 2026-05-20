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
            {"id": 1, "name": "민혁"},
            {"id": 2, "name": "FastAPI"}
        ]
    }

@app.get("/items")
def get_items():
    return {
        "items": [
            {"id": 1, "name": "Keyboard"},
            {"id": 2, "name": "Mouse"}
        ]
    }
