import json

## **************************** yemek veritabanı *****************************************
with open("meals.json") as json_file:
  datas = json.load(json_file)

datas = list(datas)

meals = []

for x in range(len(datas)):
  _meal=datas[x].get("Meal")
  _time=datas[x].get("Time")
  _hungry=datas[x].get("Hungry")

  temp_list=[_meal,_time,_hungry]
  meals.append(temp_list)


## ***************************** film-dizi veritabanı *************************************
with open("film_dizi.json") as json_file:
  datas = json.load(json_file)

datas = list(datas)

filmdizi = []

for x in range(len(datas)):
  _name=datas[x].get("name")
  _filmdizi=datas[x].get("film_dizi")
  _genre=datas[x].get("genre")

  temp_list=[_name,_filmdizi,_genre]
  filmdizi.append(temp_list)