def createQueue():
  queue = []
  return queue

def enqueue(queue, item):
  queue.append(item)

def dequeue(queue, item = ''):
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
  print('4. Kosongkan Antrian')
  print('5. Selesai')
  pilihan = input('Masukkan Pilihanmu (1, 2, 3, atau 4 lalu tekan Enter): ')
  return pilihan

def tambah(queue, limit):
  size = sizeQueue(queue)
  if size == int(limit):
    print("* Peringatan *")
    print('Antrian sudah penuh !!\n')
  else:
    reconfirm = True
    while reconfirm:
      item = input(f'Masukkan data ke-{size + 1}: ')
      if item:
        if item in queue:
          print("* Peringatan *")
          print(f'Data {item} sudah berada di dalam antrian. Mohon masukkan data yang berbeda')
        else:
          enqueue(queue, item)
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
          dequeue(queue, item)
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
  queue.sort()
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
  print()
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
    elif pilihan == '4': # Mengulang Antrian
      print('* Info *')
      print('Antrian telah dikosongkan dan program dijalankan ulang')
      main()
    elif pilihan == '5': # Program Selesai
      lanjut = False
      print('Program diakhiri. Sekian, terima kasih.\n')
      exit()
    else:
      print("* Peringatan *")
      print('Harap memilih pilihan yang tersedia!\n')

print()
print("""---   TUGAS 2 NO 2 - IMPLEMENTASI ANTRIAN DENGAN KELAS QUEUE   ---""")
main()
