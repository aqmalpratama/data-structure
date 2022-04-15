# Create a node
class Node:
  def __init__(self, kode, nama):
    self.kode = kode
    self.nama = nama
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None

  def insertAtEnd(self, kode, nama):
    new_node = Node(kode, nama)
    if self.head is None:
        self.head = new_node
        return
    last = self.head
    while (last.next):
      last = last.next
    last.next = new_node

  def deleteByCode(self, kode):
    current = self.head
    if current is not None:
      if current.kode == kode:
        self.head = current.next
        current = None
        return
    while current is not None:
      if current.kode == kode:
        break
      prev = current
      current = current.next
    if current is None:
      return
    prev.next = current.next
    current = None

  def searchByCode(self, kode):
    current = self.head
    while current is not None:
      if current.kode == kode:
        return current
      current = current.next
    return False

  def printList(self):
    temp = self.head
    while (temp):
      print(f'{temp.kode} : {temp.nama}')
      temp = temp.next

def pilihAksi():
  print("Daftar Aksi:\n 1. Tambah Data\n 2. Temukan Data\n 3. Hapus Data\n 4. Tampilkan Data\n 5. Keluar")
  pilihan = input("Masukkan pilihan Anda (1, 2, 3, 4, atau 5): ")
  return pilihan

def main():
  print("""
========================================================================
-------------------------- Selamat Datang ------------------------------
---- Program Menambah, Menemukan, dan Menampilkan Data (LinkedList) ----
========================================================================""")
  llist = LinkedList()
  print("* Format Pengisian Data*\nKode harus 3 huruf kapital\nNama harus diawali dengan kapital")
  aksi = pilihAksi()
  while aksi != "5": # selama aksi bukan 5
    if aksi == "1": # tambah data
      while True:
        kode = input("Masukkan kode: ")
        if kode:
          if len(kode) == 3:
            if kode[0].isupper() and kode[1].isupper() and kode[2].isupper():
              nama = input("Masukkan nama: ")
              if nama:
                if nama[0].isupper():
                  llist.insertAtEnd(kode, nama)
                  print("Data berhasil ditambahkan\n")
                  break
                else:
                  print("Nama harus diawali dengan kapital\n")
              else:
                print("Nama tidak boleh kosong\n")
            else:
              print("Kode harus 3 huruf kapital\n")
          else:
            print("Kode harus 3 huruf kapital\n")
        else:
          print("Kode tidak boleh kosong\n")
    elif aksi == "2": # temukan data
      kode = input("Masukkan kode yang ingin ditemukan: ")
      findData = llist.searchByCode(kode)
      if bool(findData):
        print(f"Pencarian kode {kode} berhasil ditemukan\nHasil pencarian:")
        print(f'{findData.kode} : {findData.nama}\n')
      else:
        print(f"Pencarian kode {kode} tidak ditemukan\n")
    elif aksi == "3": # hapus data
      kode = input("Masukkan kode yang ingin dihapus: ")
      findData = llist.searchByCode(kode)
      if bool(findData):
        llist.deleteByCode(kode)
        print(f"Data dengan kode {kode} berhasil dihapus\n")
      else:
        print("Data tidak ditemukan\n")
    elif aksi == "4": # tampilkan data
      print("Menampilkan semua data:")
      llist.printList()
      print('')
    else: # aksi tidak valid
      print("Pilihan tidak valid\n")
    aksi = pilihAksi()
  print("Terima kasih telah menggunakan program ini")
main()