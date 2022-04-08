class Queue:
  def __init__(self):
    self.items = []
  
  def enqueue(self, data):
    self.items.append(data)

  def dequeue(self):
    return self.items.pop(0)

  def show(self):
    return self.items

  def size(self):
    return len(self.items)
  
  def isEmpty(self):
    if self.items == []:
      return True

class Validator:
  def isNum(self, data):
    if data.isnumeric():
      return True
    else:
      print("> Data yang dimasukkan harus berupa angka!\n")
  
  def isAlpa(self, data):
    return data

  def isCmd(self, data):
    cmd_valid = ["Y", "y", "1", "N", "n", "0"]
    if data in cmd_valid:
      return True
    else:
      print("> Perintah tidak sesuai!")

def programController():
  validasi = Validator()
  while True:
    max_data = input("\nMasukkan Panjang Antrian: ")
    if(validasi.isNum(max_data)):
      break

  while True:
    pelanggan = input("Masukkan Jumlah Pelanggan Yang Datang Hari Ini: ")
    if(validasi.isNum(pelanggan)):
      break

  queue = Queue()
  print("\nDaftar Kehadiran")
  for i in range(int(pelanggan)):
    u_input = input("Masukkan Nama: ")
    if i < int(max_data):
      queue.enqueue(u_input)
      print(f"> Data [{u_input}] berhasil dimasukkan\n")
    else:
      print(f"> Data [{u_input}] gagal dimasukkan")
      print("  Antrian sudah penuh!\n")
    
  print("Data antrian pelanggan cafe:")
  count = 1
  while True:
    if queue.isEmpty():
      break
    print(f"Data {count}: {queue.dequeue()}")
    count+=1

def main():
  print("""
==================================================
----------------- Selamat Datang -----------------
-------- Program Antrian Pelanggan Cafe ----------
==================================================""")
  while True:
    programController()
    validasi = Validator()
    while True:
      u_input = input("\nApakah ingin menjalankan program ini lagi? (Y/N): ")
      if(validasi.isCmd(u_input)):
        break
    noCmd = ["N", "n", "0"]
    if u_input in noCmd:
      print("\nTerima kasih telah menjalankan program ini")
      break

main()
  