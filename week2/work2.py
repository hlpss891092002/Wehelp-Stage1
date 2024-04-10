#  --------------------task1-------------------
def find_and_print(messages, current_station):
 # your code here
  station_info = [
    {"name": "Songshan", "line": "G", "code":0 },
    {"name": "Nanjing Sanmin", "line": "G", "code":1 },
    {"name": "Taipei Arena", "line": "G", "code":2 },
    {"name": "Nanjing Fuxing", "line": "G", "code":3 },
    {"name": "Songjiang Nanjing", "line": "G", "code":4 },
    {"name": "Zhongshan", "line": "G", "code":5 },
    {"name": "Beimen", "line": "G", "code":6 },
    {"name": "Ximen", "line": "G", "code":7 },
    {"name": "Xiaonanmen", "line": "G", "code":8 },
    {"name": "Chiang Kai-Shek Memorial Hal", "line": "G", "code": 9},
    {"name": "Guting", "line": "G", "code": 10},
    {"name": "Taipower Building", "line": "G", "code": 11},
    {"name": "Gongguan", "line": "G", "code": 12},
    {"name": "Wanlong", "line": "G", "code": 13},
    {"name": "Jingmei", "line": "G", "code": 14},
    {"name": "Dapinglin", "line": "G", "code": 15},
    {"name": "Qizhang", "line": "G", "code": 16},
    {"name": "Xiaobitan", "line": "G-A", "code": 1},
    {"name": "Xindian City Hall", "line": "G", "code": 17},
    {"name": "Xindian", "line": "G", "code": 18} 
  ]
  current_station_line = ""
  current_station_code = 0

  def render_current_station_line ():
    for x in station_info:
      if x["name"]==current_station:
        return x["line"]
  def render_current_station_code ():
    for x in station_info:
      if x["name"]==current_station:
        return x["code"]
  
  current_station_line = render_current_station_line()
  current_station_code = render_current_station_code()

  def compare_station_distance():
    closest = 19
    menus = 0
    closest_message =""
    for y in messages:
      for z in station_info:
        if z["name"] in messages[y]:
          if z["line"] == current_station_line:
            menus=abs(z["code"]-current_station_code)
            if menus < closest:
              closest = menus
              closest_message=y
          else:
            menus=z["code"]+abs(16-current_station_code)
            if menus < closest:
              closest = menus
              closest_message=y
    print(closest_message)
  compare_station_distance()
 

messages={
"Leslie":"I'm at home near Xiaobitan station.",
"Bob":"I'm at Ximen MRT station.",
"Mary":"I have a drink near Jingmei MRT station.",
"Copper":"I just saw a concert at Taipei Arena.",
"Vivian":"I'm at Xindian station waiting for you."
}
find_and_print(messages, "Wanlong") # print Mary
find_and_print(messages, "Songshan") # print Copper
find_and_print(messages, "Qizhang") # print Leslie
find_and_print(messages, "Ximen") # print Bob
find_and_print(messages, "Xindian City Hall") # print Vivian

#  --------------------task2-------------------
# your code here, maybe
def book(consultants, hour, duration, criteria):
 # your code here
  consultants_list=consultants
  available_list=[]
  hour_period = set()
  def get_hour_period():
    hour_time = hour
    for y in range(duration):
      if y<=duration:
        hour_period.add(hour_time)
        hour_time+=1
  
  def insert_occupied_time():
    for x in consultants_list:
      if "occupied_time" not in x:
        x["occupied_time"]=set()
  
  def get_available_list():  
    for y in consultants_list:
      inter = y["occupied_time"]&hour_period
      if len(inter) == 0:
        available_list.append(y)

  def select_consultant(criteria):
      if len(available_list) > 0:
        chosen= available_list[0]["name"]
        if criteria=="price":
          min = available_list[0][criteria]
          for x in available_list:
            if x[criteria]<min:
              min=x[criteria]
              chosen=x["name"]
          print(chosen)
          return chosen
        elif criteria=="rate":
          max = available_list[0][criteria]
          for x in available_list:
            if x[criteria]>max:
              max=x[criteria]
              chosen=x["name"]
          print(chosen)
          return chosen
      else:
        print("No Service")

  def order_hour(consultant):
    for z in consultants_list:
      if z["name"] == consultant:
        z["occupied_time"] = z["occupied_time"]|hour_period

  get_hour_period()
  insert_occupied_time()
  get_available_list()
  the_chosen_one = select_consultant(criteria)
  order_hour(the_chosen_one)

consultants=[
{"name":"John", "rate":4.5, "price":1000},
{"name":"Bob", "rate":3, "price":1200},
{"name":"Jenny", "rate":3.8, "price":800}
]
book(consultants, 15, 1, "price") # Jenny
book(consultants, 11, 2, "price") # Jenny
book(consultants, 10, 2, "price") # John
book(consultants, 20, 2, "rate") # John
book(consultants, 11, 1, "rate") # Bob
book(consultants, 11, 2, "rate") # No Service
book(consultants, 14, 3, "price") # John

# --------------------task3-------------------
def func(*data):
  member_list=[]
  member_list_sliced=[]
  member_set_same=set()
  member_set_differ=set()
  for x in data:
    member_list.append(x)
  def slice_to_list():
    for y in member_list:
      if len(y)<3:
        member_list_sliced.append(set(y[1]))
      elif len(y)>=3:
        member_list_sliced.append(set(y[1:len(y)-1]))
  def figure_out_same():
    for y in range(len(member_list_sliced)):
      for z in range(len(member_list_sliced)):
        if y==z :
          continue
        else:
          set_y = member_list_sliced[y]
          set_z = member_list_sliced[z]
          if len(set_y&set_z) > 0:
            member_set_same.add(member_list[y])
  def print_result():
    for b in member_list:
      if b not in member_set_same:
        member_set_differ.add(b)
      else:
        continue
    if len(member_set_differ) == 0:
      print("沒有")
    else:
      for i in member_set_differ:
        print(i)
    
  slice_to_list()
  figure_out_same()
  print_result()


 #your code here
func("彭大牆", "陳王明雅", "吳明") # print 彭大牆
func("郭靜雅", "王立強", "郭林靜宜", "郭立恆", "林花花") # print 林花花
func("郭宣雅", "林靜宜", "郭宣恆", "林靜花") # print 沒有
func("郭宣雅", "夏曼藍波安", "郭宣恆") # print 夏曼藍波安

# --------------------task4-------------------
def get_number(index):
# your code here
  list = []
  num = 0
  for x in range(index+1):
    if x == 0:
      list.append(num)
    elif x % 3 == 1:
      num+=4
      list.append(num)
    elif x % 3 == 2:
      num+=4
      list.append(num)
    elif x % 3 == 0:
      num-=1
      list.append(num)
  print(list[index])

get_number(1) # print 4
get_number(5) # print 15
get_number(10) # print 25
get_number(30) # print 70

# --------------------task5-------------------
def find(spaces, stat, n):
 # your code here
  min=n
  car_num=-1
  for x in range(len(spaces)):
    menus=spaces[x]-n
    if menus<n and menus>=0 and stat[x] == 1:
      min=menus
      car_num=x
  print(car_num)

     
find([3, 1, 5, 4, 3, 2], [0, 1, 0, 1, 1, 1], 2) # print 5
find([1, 0, 5, 1, 3], [0, 1, 0, 1, 1], 4) # print-1
find([4, 6, 5, 8], [0, 1, 1, 1], 4) # print 2