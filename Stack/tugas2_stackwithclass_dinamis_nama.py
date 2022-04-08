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
    
  def size(self):
    return len(self.items)

# Maksimal Data Nama Yang dapat Ditampung
Max_Size_Name = 10
# def MaxSizeData():
#   user_input = input("Masukkan jumlah data yang ingin disimpan: ")
#   global Max_Size_Name
#   Max_Size_Name = user_input
  

class Command:
  def _init_(self, data):
    self.data = data

  startStatus = False
  saveStatus = False
  stack = Stack()

  def start(self):
    self.startStatus = True
    # MaxSizeData()
    print(f"\nMasukan Data Secara Manual, Maksimal {Max_Size_Name}!")
    print(50*"=")
    count = 1
    ableCommand = ["/save", "/delete"]
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
        delete_count = int(input("\nMasukkan jumlah data yang ingin dihapus : "))
        self.delete(delete_count)
        count-=delete_count+1
      else:
        if count > Max_Size_Name+1:
          count-=1
          print(f"Sudah mencapai batas maxsimal {Max_Size_Name}! data [{user_input}] tidak dapat dimasukkan!")
        else:
          self.stack.push(user_input)

  def save(self, count = 0):
    self.count = count
    if self.startStatus == False:
      print("\n> Program belum dimulai!")
      print(50*"=")
      return
    if self.stack.is_empty():
      print("\n> Tidak ada data yang bisa disimpan!")
      print(50*"=")
      return
    self.saveStatus = True
    print(f"\n> Daftar data yang telah disimpan berjumlah {self.count}")
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
    print(50*"=", "\n")

def programController():
  ableCommand = ["/start", "/save", "/delete"]
  user_command = input("\nMasukan Perintah: ")
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
  print("""==================================================
----------------- Selamat Datang -----------------
------- Program Input Nama Secara Dinamis --------
==================================================
 - Daftar Perintah:
    /start        : untuk menjalankan program
    /save         : untuk menghentikan program dan 
                    menampilkan data
    /delete       : untuk menghapus data terakhir
==================================================""")
  state = True
  stateTry = True
  while state:
    programController()
    yesList = ["Y", 'y', "1"]
    noList = ["N", 'n', "0"]
    stateTry = True
    while stateTry:
      feedback = input("\nApakah ingin menjalankan program ini lagi? (Y/N): ")
      if feedback in yesList or feedback in noList:
        stateTry = False
        break
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