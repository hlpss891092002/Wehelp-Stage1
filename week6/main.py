import time
import mysql.connector 
from starlette.middleware.sessions import SessionMiddleware
from fastapi import FastAPI, Request, Form, status, Response
from fastapi.responses import RedirectResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates 


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
app.add_middleware(SessionMiddleware, secret_key="some-random-string", https_only=True)
templates = Jinja2Templates(directory="templates")

error_message = {"message_error": "帳號或密碼輸入錯誤", "message_repeat_username": "帳號已被註冊"}

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="0000",
  database="website"
)

mycursor = mydb.cursor()

# mycursor.execute()

# for signup
def insert_member(name, username, password):
  sql = "INSERT INTO member (name, username, password) VALUES (%s, %s, %s)"
  val = (f"{name}", f"{username}", f"{password}")
  mycursor.execute(sql, val)
  mydb.commit()
  print(mycursor.rowcount, "record inserted.in member")

def check_repeat_username(username):
  sql = "SELECT username FROM member WHERE username = %s"
  val = (f"{username}",)
  mycursor.execute(sql, val)
  usernames_list=mycursor.fetchone ()
  if (usernames_list is None ):
    return False
  else:
    return True

#for sign in
def u_p_pair_check(username, password):
  sql = "SELECT username, password FROM member WHERE username = %s AND password = %s"
  val = (f"{username}", f"{password}")
  mycursor.execute(sql, val)
  u_p_pair=mycursor.fetchone()
  if(u_p_pair is None):
    return False
  else:
    return True
  
def get_member_data(username, password):
  mycursor.execute("SELECT id, name, username, password FROM member")
  member_data=mycursor.fetchall()
  for data in member_data:
    pair = (data[2], data[3])
    if(pair == (username, password)):
      user_state={}
      user_state["id"]=data[0]
      user_state["name"]=data[1]
      user_state["username"]=data[2]
      return user_state

#for  message
def insert_message(member_id, content):
  sql = "INSERT INTO message (member_id, content) VALUES (%s, %s)"
  val = (f"{member_id}", f"{content}")
  mycursor.execute(sql, val)
  mydb.commit()
  print(mycursor.rowcount, "record inserted in message.")

def get_all_message_data():
  mycursor.execute("""SELECT message.id, member_id, name, content
                   FROM message 
                   INNER JOIN member ON message.member_id = member.id
                   ORDER BY message.time DESC
                   """)
  messages_data = mycursor.fetchall()
  messages=[]
  # messages["id"]=messages_data[0]
  for message_data in messages_data:
    message={}
    message["message_id"]=message_data[0]
    message["member_id"]=message_data[1]
    message["name"]=message_data[2]
    message["content"]=message_data[3]
    messages.append(message)
  return messages

#for delete
def get_member_id_from_message_id(message_id):
  sql="SELECT  member_id, content FROM message WHERE id = %s "
  val=(f"{message_id}",)
  mycursor.execute(sql,val)
  member_id=mycursor.fetchone()
  message_info={}
  message_info["member_id"]=member_id[0]
  return message_info["member_id"]

def delete_row_from_message(id):
  sql = "DELETE FROM message WHERE id=%s"
  val = (f"{id}",)
  mycursor.execute(sql, val)
  mydb.commit()

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

@app.post("/createMessage")
async def create_message(request: Request, content: str = Form(None)):
  member_id=request.session["user_state"]["id"]
  insert_message(member_id, content)
  return RedirectResponse("/member",status_code=status.HTTP_303_SEE_OTHER)

@app.post("/deleteMessage")
async def delete_message(request: Request, message_id: int = Form(None)):
  member_id = get_member_id_from_message_id(message_id)
  if request.session["user_state"]["id"] == member_id:
        delete_row_from_message(message_id)
  return RedirectResponse("member", status_code=status.HTTP_303_SEE_OTHER)

@app.get("/", response_class=HTMLResponse)
async def home_page(request: Request):
  if "user_state"in request.session:
    return RedirectResponse("/member", status_code=status.HTTP_303_SEE_OTHER)
  else:
    return templates.TemplateResponse(
      request=request, name="home_page.html"
      )