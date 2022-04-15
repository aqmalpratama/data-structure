class Node:
  def __init__(self, string):
    self.string = string
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None

  def reverseString(self, string):
    string = string[::-1]
    new_node = Node(string)
    if self.head is None:
      self.head = new_node
      return
    last = self.head
    while (last.next):
      last = last.next
    last.next = new_node
  
  def printList(self):
    temp = self.head
    while (temp):
      print(f'{temp.string}')
      temp = temp.next

def main():
  print("""========================================================================
--------------------------- Selamat Datang -----------------------------
--------------- Program Membalikkan String (LinkedList) ----------------
========================================================================""")
  ll = LinkedList()
  while True:
    string = input("Masukkan string: ")
    if string:
      print('')
      ll.reverseString(string)
      print(f'Hasil membalikkan string:')
      ll.printList()
      print('')
      break
    else:
      print('* Peringatan *\nString tidak boleh kosong!\n')

  while True:
    print("""Pilih Aksi:
1. Program akan dijalankan kembali
2. Program akan diakhiri""")
    konfirmasi = input("Apakah Anda ingin menjalankan program ini kembali? (ketik 1 atau 2): ")
    if konfirmasi == '1':
      print("Baik, program dijalankan kembali\n")
      main()
    elif konfirmasi == '2':
      print('Program diakhiri. Sekian, terima kasih')
      break
    else:
      print('* Peringatan *')
      print(f'Mohon maaf, ketik dengan pilihan yang tersedia')
main()