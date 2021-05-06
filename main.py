import json

def write_json(data, filename='data.json'):
    with open(filename,'w') as f:
        json.dump(data, f, indent=4)

def check_users(users):
  f = open ('data.json', "r")
  data = json.loads(f.read())
  for e in data['users']:
    if users == e['name']:
      return e['name']

def view_task(user):
  f = open ('data.json', "r")
  data = json.loads(f.read())
  for e in data['users']:
    if e['name'] == user:
      for i, t in enumerate(e['to_do']):
        print(i, t['desc'], '=', t['state'])
  print("++++++++++++++++")
  while True:
    try:
      s = int(input("ada yg udah selesai lg blm bro?\n"))
      if s == 0:
        break
      elif s == 1:
        d = int(input("Nomer Berapa bro?\n"))
        change_state(d)
    except:
      print("Oops!")

def change_state(id):
  f = open ('data.json', "r")
  data = json.loads(f.read())
  for e in data['users']:
    if e['name'] == user:
      for i, t in enumerate(e['to_do']):
        if i == id:
          t['state'] = "Done"

  write_json(data)

def new_task(user):
  f = open ('data.json', "r")
  data = json.loads(f.read())
  for e in data['users']:
    if user == e['name']:
      new = new_to_do()
      e['to_do'].extend(new)
  write_json(data)

def new_to_do():
  to_do = []
  while True:
    desc = input("Mau ngapain lagi nih?\n")
    val = {
      "desc":desc,
      "state": "Draft"
    }
    to_do.append(val)
    try:
      s = int(input("ketik 1 kalo ada lagi, ketik 0 kalo udah\n"))
    except:
      print("Oops!")
    if s == 0:
      return to_do

def new_user():
  with open('data.json') as json_file:
    data = json.load(json_file)
    temp = data['users']

    name = input("Nama :")
    try:
      age = int(input("Umur :"))
    except:
      print("Oops!")
    to_do = new_to_do()
    y = {
            "name":name,
            "age":age,
            "to_do":to_do
        }

    temp.append(y)
    
    write_json(data)

no_user = True
i = 0
while no_user:
  if i >= 3:
    print("++++++++++++++++")
    print("Mending Daftar deh bro\n Ketik 1 Untuk Daftar\n Ketik 0 Untuk Exit")
    try:
      j = int(input())
    except:
      print("Oops!")
    if j == 1:
      new_user()
    elif j == 0:
      break

  user = input("siapa nih?\n")
  if check_users(user) == user:
    no_user = False
  i += 1

if not no_user:
  while True:
      print("++++++++++++++++")
      print("1. Lihat Task")
      print("2. Tambah Task")
      print("0. Exit")
      menu = input("Pilih Menu : ")
      print("++++++++++++++++")
      if menu == '0':
          break
      elif menu == '1':
        view_task(user)
      elif menu == '2':
        new_task(user)