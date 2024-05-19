import time
import mysql.connector 
import json
from starlette.middleware.sessions import SessionMiddleware
from fastapi import FastAPI, Request, Form, status, Response, Body
from fastapi.responses import RedirectResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel 
from typing_extensions import Annotated 
from typing import Optional
from db_SQL import insert_member, check_repeat_username, u_p_pair_check, get_member_data, insert_message, get_all_message_data, get_member_id_from_message_id, delete_row_from_message, member_api, name_update_api

name_update_api_response = {"ok":{"ok":True}, "error":{"error":True}}

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
app.add_middleware(SessionMiddleware, secret_key="some-random-string", https_only=True)
templates = Jinja2Templates(directory="templates")

error_message = {"message_error": "帳號或密碼輸入錯誤", "message_repeat_username": "帳號已被註冊"}



@app.post("/signup")
async def signup_page(request: Request, name: str=Form(None), username: str=Form(None), password: str=Form(None)):
  check_repeat_username(username)
  if (check_repeat_username(username)):
    return RedirectResponse("/error?message={message_repeat_username}".format(**error_message), status_code=status.HTTP_303_SEE_OTHER)
  else:
    insert_member(name, username, password)
    return RedirectResponse("/", status_code=status.HTTP_303_SEE_OTHER) 

@app.post("/signin")
async def signin_page(request: Request, username: str = Form(None),password: str=Form(None)):
  # return u_p_pair_check(username, password)
    if u_p_pair_check(username, password):
      request.session["user_state"]= (get_member_data(username, password))
      return RedirectResponse("/member", status_code=status.HTTP_303_SEE_OTHER)
    else:
      return RedirectResponse("error?message={message_error}".format(**error_message), status_code=status.HTTP_303_SEE_OTHER)

@app.get("/signout")
async def signout_page(request: Request):
  request.session.clear()
  print(request.session)
  return RedirectResponse("/")

@app.get("/error", response_class=HTMLResponse)
async def error_page(request: Request, message: str):
  return templates.TemplateResponse(
    request=request, name="error.html", context={"error":message},
  )

@app.get("/member")
async def member(request:Request):
  get_all_message_data()
  if "user_state" in request.session :
    print(request.session["user_state"])
    name = request.session["user_state"]["name"]
    member_id = request.session["user_state"]["id"]
    messages = get_all_message_data()
    return templates.TemplateResponse(
      request=request, name="member.html",context={"name":name, "messages": messages, "member_id":member_id}
    )
  else:
    return RedirectResponse("/", status_code=status.HTTP_303_SEE_OTHER)
    
@app.get("/api/message")
async def member(request:Request):
  if "user_state" in request.session :
    message_dict = {}
    messages = get_all_message_data()
    message_dict["messages"]=messages
    message_dict["id"]=request.session["user_state"]["id"]
    return message_dict
  else:
    return { messages: None}


@app.get("/api/member")
async def get_member_api(request: Request, username : str):
  if "user_state" in request.session:
    return member_api(username)
  else:
    return member_api(None)

@app.patch("/api/member")
async def get_member_api(request: Request, name_dict: dict):
  if "user_state" in request.session:
    update_name = name_dict["name"]
    username = request.session["user_state"]["username"]
    name_update_api(username, update_name)
    request.session["user_state"]["name"] = update_name
    return name_update_api_response["ok"]
  else:
    return name_update_api_response["error"]
@app.post("/createMessage")
async def create_message(request: Request, content: str = Form(None)):
  member_id=request.session["user_state"]["id"]
  insert_message(member_id, content)
  # return RedirectResponse("/member",status_code=status.HTTP_303_SEE_OTHER)

@app.post("/deleteMessage")
async def delete_message(request: Request, message_id: int = Form(None)):
  member_id = get_member_id_from_message_id(message_id)
  if request.session["user_state"]["id"] == member_id:
        delete_row_from_message(message_id)
  return RedirectResponse("/member", status_code=status.HTTP_303_SEE_OTHER)

@app.get("/", response_class=HTMLResponse)
async def home_page(request: Request):
  if "user_state"in request.session:
    return RedirectResponse("/member", status_code=status.HTTP_303_SEE_OTHER)
  else:
    return templates.TemplateResponse(
      request=request, name="home_page.html"
      )