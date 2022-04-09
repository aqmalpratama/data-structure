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

  def printList(self):
    temp = self.head
    if temp:
      while (temp):
        print(temp.data)
        temp = temp.next
    else:
      print("* Info *\nTumpukan kosong")

def main():
  print("""===================================================================
------------------------ Selamat Datang -----------------------------
--------------- Program Membuat Tumpukan (LinkedList) ---------------
=====================================================================""")
  ll = LinkedList()
  while True:
    jmlMaksimal = input("Masukkan jumlah maksimal tumpukan: ")
    if jmlMaksimal:
      jmlMaksimal = int(jmlMaksimal)
      if jmlMaksimal > 0:
        i = 1
        while jmlMaksimal:
          data = input(f"Masukkan data ke-{i}: ")
          if data:
            ll.insertAtEnd(data)
            print(f'Data {data} telah dimasukkan ke tumpukan')
            print('')
            jmlMaksimal -= 1
            i += 1
          else:
            print('* Peringatan *\nData tidak boleh kosong!\n')
        
        print("Isi tumpukan dari atas ke bawah:")
        ll.printList()
        print('')
        break
      else:
        print('* Peringatan *\nJumlah maksimal tumpukan tidak boleh kurang dari 1!\n')
    else:
      print('* Peringatan *\nJumlah maksimal tumpukan tidak boleh kosong!\n')
    
  while True:
    print("Pilih Aksi:\n1. Program akan dijalankan kembali\n2. Program akan diakhiri")
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