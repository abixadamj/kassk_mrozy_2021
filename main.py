import uvicorn
import fastapi
from fastapi import FastAPI, Form

app: FastAPI = FastAPI()


@app.get("/")
def index():
    html = "<h2>KASSK & Mrozy 2021</h2>"
    return fastapi.responses.HTMLResponse(html)


@app.get("/welcome/")
def welcome(user: str, welcome: str = "Python"):
    html = f"<h3>Witaj {user} - z tej strony {welcome}...</h3>"
    return fastapi.responses.HTMLResponse(html)


@app.get("/welcome-json/{user}")
def welcome(user: str, welcome: str = "Python"):
    return {
        "type": "WELCOME",
        "user_name": user,
        "welcome by": welcome,
    }


@app.get("/auth")
def auth_get():
    html = """<h2>KASSK & MROZY</h2><hr/>
    <form action="/auth/" enctype="multipart/form-data" method="post">

    <label>Wypełnij Twoje AUTH_ID:</label>
    <input type="text" name="auth_id" required minlength="5" size="20">
    <hr/>
    <input type="submit" value="Wyślij dane do centrali">
    </form>

    """
    return fastapi.responses.HTMLResponse(html)


@app.post("/auth")
def auth_test(auth_id: str = Form(...)):
    if auth_id == "KASSK_MROZY":
        html = "<h2>SUPER</h2>"
    else:
        html = "<h3>Error !!!</h3>"
    return fastapi.responses.HTMLResponse(html)


if __name__ == "__main__":
    uvicorn.run(app)
