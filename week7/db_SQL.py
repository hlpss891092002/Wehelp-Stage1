import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="0000",
  database="website"
)

mycursor = mydb.cursor()

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
  if val[1] == "None":
    return
  else:
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

# for api
def member_api(username):
  sql = "SELECT id, name, username FROM member WHERE username = %s"
  val = (f"{username}",)
  mycursor.execute(sql, val)
  user_data=mycursor.fetchone ()
  if (user_data is None):
    user_api ={
      "data":"null"
    }
    return user_api
  else:
    user_api ={
      "data":{
        "id":f"{user_data[0]}",
        "name":f"{user_data[1]}",
        "username":f"{user_data[2]}"
      }
    }
    return user_api
  print(user_api)