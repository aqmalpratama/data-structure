# Create a node
class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None

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

  def insertAtAfter(self, key, data):
    new_node = Node(data)
    current = self.head
    if current is not None:
      if current.data == key:
        self.insertAtEnd(data)
        return
    while current is not None:
      if current.data == key:
        break
      prev = current
      current = current.next
    if current is None:
      return
    prev.next = current.next
    current = new_node

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

  def sortDataToArray(self):
    size = self.getCount()
    arr = []
    temp = self.head
    while (temp):
      arr.append(temp.data)
      temp = temp.next
    # arr.sort()
    i = 0
    while (i < size):
      print(f'{arr[i]}')
      i += 1

def pilihAksi():
  print("Daftar Aksi:\n1. Tambah Data\n2. Hapus Data\n3. Tampilkan Data\n4. Keluar")
  pilihan = input("Masukkan pilihan Anda (1, 2, 3, atau 4): ")
  return pilihan

def printTitle(arr, aksi):
  txt = ''
  i = 0
  size = len(arr)
  while i < size:
    if i != size - 1:
      txt += arr[i] + ', '
    else:
      txt += arr[i]
    i+=1
  arr.clear()
  if aksi == '1':
    print(f'Isi data setelah {txt} ditambah: ')
  elif aksi == '2':
    print(f'Isi data setelah {txt} dihapus: ')
    
def main():
  print("""========================================================================================
---------------------------------- Selamat Datang --------------------------------------
---- Program Menambah, Menemukan, Menampilkan beserta Mengurutkan Data (LinkedList) ----
========================================================================================""")
  llist = LinkedList()
  aksi = pilihAksi()
  arrInsert = []
  arrDelete = []
  aksiTerakhir = ''
  while aksi != "4": # selama aksi bukan 4
    if aksi == "1": # tambah data
      while True:
        data = input("Masukkan data: ")
        if data:
          llist.insertAtEnd(data)
          print(f'Data {data} berhasil ditambahkan\n')
          arrInsert.append(data)
          aksiTerakhir = '1'
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
          arrDelete.append(data)
          aksiTerakhir = '2'
        else:
          print(f'Data {data} tidak ditemukan\n')
      else:
        print('Data kosong\n')
    elif aksi == "3": # tampilkan data
      if llist.isEmpty() == False:
        if aksiTerakhir == '1':
          printTitle(arrInsert, aksiTerakhir)
        elif aksiTerakhir == '2':
          printTitle(arrDelete, aksiTerakhir)
        else:
          print('Isi data saat ini: ')
        llist.sortDataToArray()
        aksiTerakhir = '3'
      else:
        print("Data kosong")
      print('')

    elif aksi == "5":
      if llist.isEmpty() == False:
        dataKey = input("Masukkan kata kunci data yang ingin ditambah setelahnya: ")
        findData = llist.searchData(dataKey)
        if bool(findData):
          while True:
            data = input("Masukkan data: ")
            if data:
              llist.insertAtAfter(dataKey, data)
              print(f'Data {data} berhasil ditambahkan setelah {dataKey}\n')
              arrInsert.append(data)
              aksiTerakhir = '1'
              break
            else:
              print("* Peringatan *\nData harus diisi\n")
        else:
          print(f'Data {data} tidak ditemukan\n')
      else:
        print('Data kosong\n')

    else: # aksi tidak valid
      print("Pilihan tidak valid\n")
    aksi = pilihAksi()
  print("Terima kasih telah menggunakan program ini\n")
main()