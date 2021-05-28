import uvicorn
import fastapi
from fastapi import FastAPI

app: FastAPI = FastAPI()

@app.get("/")
def index():
    html = "<h2>KASSK & Mrozy 2021</h2>"
    return fastapi.responses.HTMLResponse(html)

@app.get("/welcome")
def welcome(user: str, welcome: str = "Python"):
    html = f"Witaj {user} - z tej strony {welcome}..."
    return fastapi.responses.HTMLResponse(html)

if __name__ == "__main__":
    uvicorn.run(app)
