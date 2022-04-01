class Stack:
  def __init__(self):
    self.items = []

  def is_empty(self):
    if self.items == []:
      return True

  def push(self, data):
    self.items.append(data)
 
  def pop(self):
    return self.items.pop()

  def clear(self):
    return self.items.clear()
    
  def size(self):
    return len(self.items)

class Command:
  def _init_(self, data):
    self.data = data

  startStatus = False
  saveStatus = False
  stack = Stack()

  def start(self):
    self.startStatus = True
    print(50*"=")
    print("Masukan Data Secara Manual!")
    print(50*"=")
    count = 1
    ableCommand = ["/start", "/save", "/delete"]
    while self.saveStatus == False:
      user_input = input(f"Data ke-{count}: ")
      if user_input[0] == "/":
        if user_input not in ableCommand:
          print("Perintah tidak ditemukan!")
          continue
      count+=1
      if user_input == "/save":
        count-=2
        self.save(count)
        return
      elif user_input == "/delete":
        delete_count = int(input("Masukkan jumlah data yang ingin dihapus : "))
        self.delete(delete_count)
        count-=delete_count+1
      else:
        self.stack.push(user_input)

  def save(self, count = 0):
    self.count = count
    if self.startStatus == False:
      print("> Program belum dimulai!")
      print(50*"=")
      return
    if self.stack.is_empty():
      print("> Tidak ada data yang bisa disimpan!")
      print(50*"=")
      return
    self.saveStatus = True
    print(f"> Daftar data yang telah disimpan berjumlah {self.count}")
    print(50*"=")
    count = 1
    while self.stack.is_empty() != True:
      print(f"Nomor {count}: {self.stack.pop()}")
      count+=1
    print(50*"=")

  def delete(self, data = 1):
    if self.stack.is_empty():
      print("> Tidak ada data yang bisa dihapus!")
      print(50*"=")
      return
    for i in range(data):
      temp = self.stack.pop()
      print(f"> Data: {temp} dihapus!")
    print(50*"=")

def programController():
  ableCommand = ["/start", "/save", "/delete"]
  user_command = input("Masukan Perintah: ")
  if user_command not in ableCommand:
    print("> Perintah tidak sesuai!")
    print(50*"=")
    return True
  command = Command()
  if user_command == "/start":
    command.start()
  if user_command == "/save":
    command.save()
  if user_command == "/delete":
    command.delete()

def main():
  print("""
==================================================
----------------- Selamat Datang -----------------
------- Program Input Nama Secara Dinamis --------
==================================================
 - Daftar Perintah:
    /start        : untuk menjalankan program
    /save         : untuk menghentikan program dan 
                    menampilkan data
    /delete       : untuk menghapus data terakhir
==================================================
  """)
  state = True
  stateTry = True
  while state:
    programController()
    yesList = ["Y", 'y', "1"]
    noList = ["N", 'n', "0"]
    stateTry = True
    while stateTry:
      feedback = input("Apakah ingin menjalankan program ini lagi? (Y/N): ")
      if feedback in yesList or feedback in noList:
        stateTry = False
        break
      print(50*"=")
      print("Perintah tidak sesuai!")
      print("Silahkan coba kembali!")
      print(50*"=")
    if feedback in yesList:
      state = True
    elif feedback in noList:
      state = False
  print(50*"=")
  print("Terimakasih telah menggunakan program ini >_<")
  print(50*"=")
main()