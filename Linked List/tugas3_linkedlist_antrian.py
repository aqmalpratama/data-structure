# Create a node
class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None

  def insertAtEnd(self, data):
    new_node = Node(data)
    if self.head is None:
        self.head = new_node
        return
    last = self.head
    while (last.next):
      last = last.next
    last.next = new_node

  def searchData(self, data):
    current = self.head
    while current is not None:
      if current.data == data:
        return current
      current = current.next
    return False

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

  def printList(self):
    temp = self.head
    while (temp):
      print(f'{temp.data}')
      temp = temp.next

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

def pilihAksi():
  print("Daftar Aksi:\n1. Tambah Data\n2. Hapus Data\n3. Tampilkan Data\n4. Keluar")
  pilihan = input("Masukkan pilihan Anda (1, 2, 3, atau 4): ")
  return pilihan

def main():
  print("""
========================================================================
-------------------------- Selamat Datang ------------------------------
---- Program Menambah, Menemukan, dan Menampilkan Data (LinkedList) ----
========================================================================""")
  while True:
    jmlMaksimal = input("Masukkan jumlah maksimal data: ")
    if jmlMaksimal:
      jmlMaksimal = int(jmlMaksimal)
      if jmlMaksimal > 0:
        break
      else:
        print('* Peringatan *\nJumlah maksimal harus lebih dari 0\n')
    else:
      print("* Peringatan *\nJumlah maksimal harus diisi\n")

  llist = LinkedList()
  aksi = pilihAksi()
  while aksi != "4": # selama aksi bukan 4
    if aksi == "1": # tambah data
      size = llist.getCount()
      while True:
        data = input("Masukkan data: ")
        if data:
          if size < jmlMaksimal:
            llist.insertAtEnd(data)
            print(f'Data {data} berhasil ditambahkan\n')
            break
          else:
            print("* Peringatan *\nJumlah maksimal data sudah tercapai\n")
            break
        else:
          print("* Peringatan *\nData harus diisi\n")
    elif aksi == "2": # hapus data
      if llist.isEmpty() == False:
        data = input("Masukkan data yang ingin dihapus: ")
        findData = llist.searchData(data)
        if bool(findData):
          llist.deleteData(data)
          print(f'Data {data} berhasil dihapus\n')
        else:
          print(f'Data {data} tidak ditemukan\n')
      else:
        print('Data kosong\n')
    elif aksi == "3": # tampilkan data
      if llist.isEmpty() == False:
        print('Isi data saat ini: ')
        llist.printList()
      else:
        print("Data kosong")
      print('')
    else: # aksi tidak valid
      print("Pilihan tidak valid\n")
    aksi = pilihAksi()
  print("Terima kasih telah menggunakan program ini\n")
main()