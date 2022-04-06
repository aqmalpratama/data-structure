def tambah(queue, limit, deletedIndex):
  newQueue = [x for x in queue if x != "kosong"]
  print(f'size {len(newQueue)}, limit {limit}, index yang dihapus ada {len(deletedIndex)}')
  deletedIndex.sort()
  size = index = len(newQueue)
  if len(newQueue) == int(limit):
    print('Antrian sudah penuh')
  else:
    reconfirm = True
    while reconfirm:
      item = input('Masukkan data yang ingin ditambahkan: ')
      if item:
        if item in queue:
          print(f'Data {item} sudah berada didalam antrian. Mohon masukkan data yang berbeda')
        else:
          if len(deletedIndex) > 0:
            queue[deletedIndex[0]] = item
            deletedIndex.pop(0)
            print(f'Data {item} berhasil masuk ke dalam antrian\n')
          else:
            queue.append(item)
            print(f'Data {item} berhasil masuk ke dalam antrian\n')
          reconfirm = False
      else:
        print('Data yang ingin ditambahkan tidak boleh kosong\n')
        reconfirm = False
  # return len(queue)

def hapus(queue):
  reconfirm = True
  while reconfirm:
    if len(queue) > 0:
      item = input('Data yang ingin dihapus: ')
      if item:
        if item in queue:
          index = queue.index(item)
          queue[index] = 'kosong'
          reconfirm = False
          print(f'Data {item} berhasil dihapus dari antrian.')
          print(f'index yang dihapus-{index}')
        else:
          print(f'Data {item} tidak ada di dalam antrian.')
      else:
        print('Data yang ingin dihapus tidak boleh kosong')
    else:
      print('Antrian kosong')
      reconfirm = False
      index = 0
    return index

def tampil(queue):
  newQueue = [x for x in queue if x != "kosong"]
  print(f'data queue : {queue}')
  print(f'data newqueue : {newQueue}')
  print('Isi Antrian: ')
  size = len(newQueue)
  # queue.sort()
  if size != 0:
    i = 0
    while i < size:
      if i != size - 1:
        print(newQueue[i], end=" - ")
      else:
        print(newQueue[i])
      i+=1
  else:
    print('Antrian Kosong')
  print()

def pilihMenu():
  print('Menu:')
  print('1. Tambah Data')
  print('2. Hapus Data')
  print('3. Tampilkan Data')
  print('4. Selesai')
  pilihan = input('Masukkan Pilihanmu (1, 2, 3, atau 4): ')
  return pilihan

def main():
  print('---- Program Menambah dan Menghapus Data (Antrian) ----')
  queue = []
  deletedIndex = []

  getIndex = 0
  limit = input('Masukkan limit antrian: ')
  selesai = False
  while selesai == False:
    pilihan = pilihMenu()
    if pilihan == '1': # Tambah Data
      tambah(queue, limit, deletedIndex)
    elif pilihan == '2': # Hapus Data
      getIndex = hapus(queue)
      deletedIndex.append(getIndex)
    elif pilihan == '3': # Tampil Data
      tampil(queue)
    elif pilihan == '4': # Program Selesai
      selesai = True
      print('Program diakhiri. Sekian, terima kasih.\n')
    else:
      print('Pilihan tidak tersedia. Harap memilih pilihan yang tersedia!\n')
    print(f'Data deletedIndex : {deletedIndex}')
main()