# Create a node
class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None

  # Insert at the beginning
  def insertAtBeginning(self, data):
    new_node = Node(data)
    new_node.next = self.head
    self.head = new_node

  def insertAtAfter(self, key, data):
    new_node = Node(data)
    current = self.head
    while current is not None:
      if current.data == key:
        new_node.next = current.next
        current.next = new_node
        return
      current = current.next
    return False

  # Insert at the end
  def insertAtEnd(self, data):
    new_node = Node(data)
    if self.head is None:
        self.head = new_node
        return
    last = self.head
    while (last.next):
      last = last.next
    last.next = new_node

  # Deleting
  def deleteData(self, data):
    current = self.head
    if current is not None:
      if current.data == data:
        self.head = current.next
        current = None
        return
    while current is not None:
      if current.data == data:
        break
      prev = current
      current = current.next
    if current is None:
      return
    prev.next = current.next
    current = None

  def deleteFirst(self):
    temp = self.head
    data = temp.data
    self.head = temp.next
    temp = None
    return data

  def deleteLast(self):
    temp = self.head
    while (temp.next):
      prev = temp
      temp = temp.next
    data = temp.data
    prev.next = None
    temp = None
    return data

  # Search an element
  def searchData(self, key):
    current = self.head
    while current is not None:
      if current.data == key:
        return current
      current = current.next
    return False

  def printFromFirst(self):
    temp = self.head
    count = 1
    while (temp):
      print(f"No.{count} {temp.data}")
      count+=1
      temp = temp.next

  def printFromLast(self):
    temp = self.head
    arr = []
    while (temp):
      arr.append(temp.data) 
      temp = temp.next
    count = 1
    i = len(arr)
    while (i != 0):
      print(f"No.{count} {arr[i-1]}")
      count+=1
      i-=1

  def isEmpty(self):
    temp = self.head
    if temp is None:
      return True
    else:
      return False

  def getCount(self):
    temp = self.head
    count = 0
    while (temp):
      count += 1
      temp = temp.next
    return count

def menuUtama():
  print("\nDaftar Aksi:\n1. Tambah Data\n2. Hapus Data\n3. Tampilkan Data\n4. Keluar")
  pilihan = input("Masukkan pilihan Anda (1, 2, 3, atau 4): ")
  return pilihan

def pilihAksiTambah():
  print("\nPilihan Tambah:\n1. Tambah Data di Depan\n2. Tambah Data di Belakang\n3. Tambah Data Setelah Kata Kunci\n4. Kembali")
  pilihan = input("Masukkan pilihan Anda: ")
  return pilihan

def pilihAksiHapus():
  print("\nPilihan Hapus:\n1. Hapus Data di Depan\n2. Hapus di Belakang\n3. Hapus Data berdasarkan kata kunci\n4. Kembali")
  pilihan = input("Masukkan pilihan Anda: ")
  return pilihan

def pilihAksiTampilkan():
  print("\nPilihan Tampilan:\n1. Tampilkan data pertama ke terakhir\n2. Tampilkan data terakhir ke pertama\n3. Kembali")
  pilihan = input("Masukkan pilihan Anda: ")
  return pilihan

def main():
  print("""
========================================================================
-------------------------- Selamat Datang ------------------------------
---- Program Menambah, Menemukan, dan Menampilkan Data (LinkedList) ----
========================================================================""")
  llist = LinkedList()
  aksi = menuUtama()
  while aksi != "4": # selama aksi bukan 4
    if aksi == "1": # tambah data
      aksiTambah = pilihAksiTambah()
      if aksiTambah == "1": #didepan
        data = input("Masukkan data: ")
        if data:
          llist.insertAtBeginning(data)
          print(f'Data {data} berhasil ditambahkan')
        else:
          print("* Peringatan *\nData harus diisi")
      elif aksiTambah == "2": #diakhir
        data = input("Masukkan data: ")
        if data:
          llist.insertAtEnd(data)
          print(f'Data {data} berhasil ditambahkan')
        else:
          print("* Peringatan *\nData harus diisi")
      elif aksiTambah == "3": #withKey
        if llist.isEmpty() == False:
          dataKey = input("Masukkan kata kunci data yang ingin ditambah setelahnya: ")
          findData = llist.searchData(dataKey)
          if bool(findData):
            while True:
              data = input("Masukkan data: ")
              if data:
                llist.insertAtAfter(dataKey, data)
                print(f'Data {data} berhasil ditambahkan setelah {dataKey}')
                break
              else:
                print("* Peringatan *\nData harus diisi")
          else:
            print(f'Data {data} tidak ditemukan')
        else:
          print('Data kosong')
      elif aksiTambah == "4":
        menuUtama()
      else: # aksi tidak valid
        print("Pilihan tidak valid") 
    elif aksi == "2": # hapus data
      if llist.isEmpty() == False:
        aksiHapus = pilihAksiHapus()
        if aksiHapus == "1": #depan
          data = llist.deleteFirst()
          print(f'Data {data} berhasil dihapus')
        elif aksiHapus == "2": #belakang
          if llist.getCount() > 1:
            data = llist.deleteLast()
          else:
            data = llist.deleteFirst()
          print(f'Data {data} berhasil dihapus')
        elif aksiHapus == "3": #key
          data = input("Masukkan data yang ingin dihapus: ")
          findData = llist.searchData(data)
          if bool(findData):
            llist.deleteData(data)
            print(f'Data {data} berhasil dihapus')
          else:
            print(f'Data {data} tidak ditemukan')
        elif aksiHapus == "4":
          menuUtama()
        else: # aksi tidak valid
          print("Pilihan tidak valid")  
      else:
        print('Data kosong')
    elif aksi == "3": # tampilkan data
      if llist.isEmpty() == False:
        aksiPilihan = pilihAksiTampilkan()
        if aksiPilihan == "1":
          llist.printFromFirst()
        elif aksiPilihan == "2":
          llist.printFromLast()
        elif aksiPilihan == "3":
          menuUtama()
        else:
          print("Pilihan tidak valid")
      else:
        print("Data kosong")
    else: # aksi tidak valid
      print("Pilihan tidak valid")
    aksi = menuUtama()
  print("Terima kasih telah menggunakan program ini\n")
main()