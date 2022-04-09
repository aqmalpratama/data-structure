def createQueue():
  queue = []
  return queue

def addItem(queue, item):
  queue.append(item)

def removeItem(queue, item = ''):
  if item:
    return queue.remove(item)
  else:
    return queue.pop(0)

def sizeQueue(queue):
  return len(queue)

def pilihMenu():
  print('Menu:')
  print('1. Tambah Data')
  print('2. Hapus Data')
  print('3. Tampilkan Data')
  print('4. Selesai')
  pilihan = input('Masukkan Pilihanmu (1, 2, 3, atau 4): ')
  return pilihan

def tambah(queue, limit):
  size = sizeQueue(queue)
  if size == int(limit):
    print("* Peringatan *")
    print('Antrian sudah penuh !!\n')
  else:
    reconfirm = True
    while reconfirm:
      item = input(f'Masukkan data pada indeks ke-{size + 1}: ')
      if item:
        if item in queue:
          print("* Peringatan *")
          print(f'Data {item} sudah berada di dalam antrian. Mohon masukkan data yang berbeda')
        else:
          queue.append(item)
          print("* Info *")
          print(f'Data {item} berhasil masuk ke dalam antrian\n')
          reconfirm = False
      else:
        print("* Peringatan *")
        print('Data yang ingin ditambahkan tidak boleh kosong\n')
        reconfirm = False

def hapus(queue):
  reconfirm = True
  while reconfirm:
    if sizeQueue(queue) > 0:
      item = input('Data yang ingin dihapus: ')
      if item:
        if item in queue:
          removeItem(queue, item)
          print('* Info *')
          print(f'Data {item} berhasil dihapus dari antrian\n')
          reconfirm = False
        else:
          print('* Peringatan *')
          print(f'Data {item} tidak ada di dalam antrian.')
      else:
        print('* Peringatan *')
        print('Data yang ingin dihapus tidak boleh kosong')
    else:
      print('* Peringatan *')
      print('Antrian kosong, lakukan tambah data terlebih dahulu')
      reconfirm = False

def tampil(queue):
  print('Isi Antrian: ')
  size = sizeQueue(queue)
  if size != 0:
    i = 0
    while i < size:
      if i != size - 1:
        print(queue[i], end=" - ")
      else:
        print(queue[i])
      i+=1
  else:
    print('* Peringatan *')
    print('Antrian kosong, lakukan tambah data terlebih dahulu')
  print()

def main():
  print("""
===================================================================
------------------------ Selamat Datang ---------------------------
---- Program Menambah, Menghapus, dan Menampilkan Data (Queue) ----
===================================================================
""")
  queue = createQueue()
  limit = input('Masukkan limit antrian: ')
  lanjut = True
  while lanjut:
    pilihan = pilihMenu()
    if pilihan == '1': # Tambah Data
      tambah(queue, limit)
    elif pilihan == '2': # Hapus Data
      hapus(queue)
    elif pilihan == '3': # Tampil Data
      tampil(queue)
    elif pilihan == '4': # Program Selesai
      lanjut = False
      print('Program diakhiri. Sekian, terima kasih.\n')
    else:
      print("* Peringatan *")
      print('Harap memilih pilihan yang tersedia!\n')
main()
