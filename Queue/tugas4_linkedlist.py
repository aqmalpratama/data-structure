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
  print("Daftar Aksi:\n1. Tambah Data\n2. Temukan Data\n3. Hapus Data\n4. Tampilkan Data\n5. Keluar")
  pilihan = input("Masukkan pilihan Anda (1, 2, 3, 4, atau 5 lalu tekan Enter): ")
  return pilihan

def main():
  print()
  print("""---   TUGAS 2 NO 4 - IMPLEMENTASI INPUT 2 DATA(KODE DAN NAMA) DENGAN LINKED LIST   ---""")

  llist = LinkedList()
  print("\n* Format Pengisian Data*\nKode harus 3 huruf kapital\nNama harus diawali dengan kapital\n")
  aksi = pilihAksi()
  while aksi != "5": # selama aksi bukan 5
    if aksi == "1": # tambah data
      while True:
        kode = input("Masukkan kode: ")
        if bool(kode) == False:
          print("Kode tidak boleh kosong")
        if bool(kode) == True and len(kode) != 3:
          print("Kode harus 3 huruf kapital\n")
        if bool(kode) == True and len(kode) == 3 and kode.isupper() == False:
          print("Kode harus 3 huruf kapital\n")

        if bool(kode) == True and (len(kode) == 3 and kode.isupper() == True):
          nama = input("Masukkan nama: ")
          if bool(nama) == False:
            print("Nama tidak boleh kosong")
            print("Harap isi kode kembali\n")
          if bool(nama) == True and nama[0].isupper() == False:
            print("Nama harus diawali dengan kapital")
            print("Harap isi kode kembali\n")
          if bool(nama) == True and nama[0].isupper() == True:
            llist.insertAtEnd(kode, nama)
            print("Data berhasil ditambahkan\n")
            break
    
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