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


def drop_table(table):
  mycursor.execute(f"DROP TABLE {table}")

def delete_row(table, id):
  mycursor.execute(f"DELETE FROM {table} WHERE id={id}")
  mydb.commit()


# for signup
def insert_member(name, username, password):
  sql = "INSERT INTO member (name, username, password) VALUES (%s, %s, %s)"
  val = (f"{name}", f"{username}", f"{password}")
  mycursor.execute(sql, val)
  mydb.commit()
  print(mycursor.rowcount, "record inserted.in member")

def check_repeat_username(username):
  mycursor.execute("""SELECT username FROM member """)
  usernames_list=mycursor.fetchall ()
  for user in usernames_list:
    name_of_user = user[0]
    if(name_of_user == username):
      return True
  return False

#for sign in
def u_p_pair_check(username, password):
  mycursor.execute("SELECT username, password FROM member")
  u_p_pair=mycursor.fetchall()
  for pair in u_p_pair:
    if(pair == (username, password)):
      return True
  return False
  
def get_member_data(username, password):
  mycursor.execute("SELECT id, name, username, password FROM member")
  member_data=mycursor.fetchall()
  for data in member_data:
    pair = (data[2], data[3])
    if(pair == (username, password)):
      return data[0:3]

#for  message
def insert_message(member_id, content):
  sql = "INSERT INTO message (member_id, content) VALUES (%s, %s)"
  val = (f"{member_id}", f"{content}")
  mycursor.execute(sql, val)
  mydb.commit()
  print(mycursor.rowcount, "record inserted in message.")

def get_all_message_data():
  mycursor.execute("""SELECT name, content 
                   FROM message 
                   INNER JOIN member ON message.member_id = member.id
                   ORDER BY message.time DESC
                   """)
  messages = mycursor.fetchall()
  return messages
  for data in all_data:
    print(data)

@app.post("/signup")
async def signup_page(request: Request, name: str=Form(None), username: str=Form(None), password: str=Form(None)):
  if (check_repeat_username(username)):
    return RedirectResponse("/error?message={message_repeat_username}".format(**error_message), status_code=status.HTTP_303_SEE_OTHER)
  else:
    insert_member(name, username, password)
    return RedirectResponse("/", status_code=status.HTTP_303_SEE_OTHER) 

@app.post("/signin")
async def signin_page(request: Request, username: str = Form(None),password: str=Form(None)):
  if u_p_pair_check(username, password):
    request.session["user_state"]= (get_member_data(username, password))
    print(request.session)
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
  print(mydb)
  return templates.TemplateResponse(
    request=request, name="error.html", context={"error":message},
  )

@app.get("/member")
async def member(request:Request):
  get_all_message_data()
  if "user_state" in request.session :
    print(request.session)
    print(request.session["user_state"])
    name = request.session["user_state"][1]
    messages = get_all_message_data()
    print(messages)
    return templates.TemplateResponse(
      request=request, name="member.html",context={"name":name, "messages": messages}
    )
  else:
    return RedirectResponse("/", status_code=status.HTTP_303_SEE_OTHER)

@app.post("/createMessage")
async def create_message(request: Request, content: str = Form(None)):
  member_id=request.session["user_state"][0]
  print(request.session["user_state"])
  print(member_id)
  print(content)
  insert_message(member_id, content)
  return RedirectResponse("/member",status_code=status.HTTP_303_SEE_OTHER)

@app.get("/", response_class=HTMLResponse)
async def home_page(request: Request):
  if "user_state"in request.session:
    return RedirectResponse("/member", status_code=status.HTTP_303_SEE_OTHER)
  else:
    return templates.TemplateResponse(
      request=request, name="home_page.html"
      )