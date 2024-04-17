import urllib.request as request
import json
import csv
src1="https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-1"
src2="https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-2"
ASSIGNMENT_LIST=[]
MRT_list=[]
MRT_and_spot={}
def get_assignment1_data():
  with request.urlopen(src1) as response:
    data=json.load(response)
  # data=response.read().decode("utf-8")
  assignment1=data["data"]["results"]
  for list1 in assignment1:
    jpg_index=list1["filelist"].lower().index("jpg")
    list1["photo"]=list1["filelist"][0:jpg_index+3]
    ASSIGNMENT_LIST.append(list1)
def render_assignment2_data_to_assignment_list():
  with request.urlopen(src2) as response:
    data=json.load(response)
    # data=response.read().decode("utf-8")
  assignment2=data["data"]
  assignment2List=[]
  for list2 in assignment2:
    list2["address"]=list2["address"].split()
    list2["district"]=list2["address"][1][0:3]
    assignment2List.append(list2)
  for list1 in ASSIGNMENT_LIST:
    for list2 in assignment2List:
      if (list1["SERIAL_NO"] == list2["SERIAL_NO"] ):
        list1.update(list2)
def distinct_from_station():
  MRT_set=set()
  for dict in ASSIGNMENT_LIST:
    MRT_set.add(dict["MRT"])
  for item in MRT_set:
    MRT_list.append(item)
  for item in MRT_list:
    MRT_and_spot[item]=[]
  for item in ASSIGNMENT_LIST:
    for title in MRT_list:
      if item["MRT"]==title:
        MRT_and_spot[title].append(item["stitle"])   
  for item in MRT_and_spot:
    MRT_and_spot[item]=",".join(MRT_and_spot[item])
    print
get_assignment1_data()
render_assignment2_data_to_assignment_list()
distinct_from_station()


with open("spot.csv", mode="w", encoding="utf-8", newline="") as csvfile:
  writer = csv.writer(csvfile)
  for row in ASSIGNMENT_LIST:
    writer.writerow([row["stitle"], row["district"], row["longitude"], row["latitude"], row["photo"]])
with open("mrt.csv", mode="w", encoding="utf-8", newline="") as csvfile:
  writer = csv.writer(csvfile)
  for key in MRT_and_spot:
    csvfile.write(key+","+MRT_and_spot[key]+"\n")