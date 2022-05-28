import time

class Node:
  def __init__(self, string):
    self.string = string
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None

  def reverseString(self, string):
    length = len(string)
    arr = []
    for i in range(length):
      arr.append(string[i])
    string = ""
    print("Proses membalik kata atau kalimat")
    for i in range(length):
      string += arr.pop()
      time.sleep(0.2)
      print(string)
    return string
  
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
      print('\n\n')
      print(f'String yang telah dibalik: {ll.reverseString(string)}')
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
      exit()
    else:
      print('* Peringatan *')
      print(f'Mohon maaf, ketik dengan pilihan yang tersedia')
main()