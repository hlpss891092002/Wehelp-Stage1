from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from typing_extensions import Annotated

app = FastAPI()

# correct_pair = [{"username": "test"}, {"password": "test"}]

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_home_page(request: Request):
    return templates.TemplateResponse(
         request=request, name="user.html"
    )
# @app.post("/login/")
# async def login(username: Annotated[str, Form], password: Annotated[str, Form]):
#     return {username}

# @app.get("/items/{id}", response_class=HTMLResponse)
# async def read_item(request: Request, id: str):
#     return templates.TemplateResponse(
#         request=request, name="item.html", context={"id": id}
#     )

# @app.post("/submit")
# async def submit_form(username: str = Form(...), password: str = Form(...)):
#     return {"username": username, "password": password}




