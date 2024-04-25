import time
from starlette.applications import Starlette
from starlette.middleware import Middleware
from starlette.middleware.sessions import SessionMiddleware
from starlette.middleware.httpsredirect import HTTPSRedirectMiddleware
from starlette.middleware.trustedhost import TrustedHostMiddleware
from fastapi import FastAPI, Request, Form, status, Response, APIRouter 
from fastapi.responses import RedirectResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel, Field
from typing import Annotated, Union

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
app.add_middleware(SessionMiddleware, secret_key="some-random-string", https_only=True)
templates = Jinja2Templates(directory="templates")

error_message = {"message_empty": "請輸入帳號、密碼", "message_error": "帳號、密碼輸入錯誤"}
user = {"username":"test", "password": "test"}

@app.post("/signin")
async def signin_in(request: Request, username: str = Form(None), password: str = Form(None),  ):
    # return {username is None and password is None }
    if username is None or password is None:
        return RedirectResponse("/error?message={message_empty}".format(**error_message),status_code=status.HTTP_303_SEE_OTHER ) 
    
    elif username == user["username"] and password == user["password"]:
       request.session["SIGNED_IN"] = "TRUE"
       redirect_url = request.url_for("member_page")
       return RedirectResponse(redirect_url, status_code=status.HTTP_303_SEE_OTHER)
      
    elif username != "test" or password != "test":
        return RedirectResponse("/error?message={message_error}".format(**error_message),status_code=status.HTTP_303_SEE_OTHER )  



@app.get("/signout", status_code=status.HTTP_303_SEE_OTHER)
async def sign_out(request : Request):
        request.session["SIGNED_IN"] = "FALSE"
        return RedirectResponse("/", status_code=status.HTTP_303_SEE_OTHER)

# 
@app.get("/member", response_class=HTMLResponse)
async def member_page(request: Request):
    if request.session["SIGNED_IN"] == "FALSE":
        return RedirectResponse("/", status_code=status.HTTP_303_SEE_OTHER)
    return templates.TemplateResponse(
        request=request, name="member.html"
    )

@app.get("/error", response_class=HTMLResponse)
async def error_page(request: Request, message: str):
    return templates.TemplateResponse(
        request=request, name="error.html", context = {"error":message }
    )

@app.get("/", response_class=HTMLResponse)
async def read_home_page(request: Request):
    if request.session["SIGNED_IN"] == "TRUE":
        return RedirectResponse("/member") 
    else:
        request.session["SIGNED_IN"] = "FALSE"
        return templates.TemplateResponse(
            request=request, name="user.html"
        )


@app.get("/square/{number}", response_class=HTMLResponse)
async def render_square_number(request: Request, number: int):
    return templates.TemplateResponse(
        request=request, name="square.html", context = {"square": number**2}
    )
    pass
