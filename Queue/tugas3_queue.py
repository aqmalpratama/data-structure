def createArray():
  array = list()
  return array

def addItem(array, item):
  array.append(item)

def removeItem(array, item = ''):
  if item:
    return array.remove(item)
  else:
    return array.pop(0)

def pilihMenu():
  print('Menu:')
  print('1. Tambah Data')
  print('2. Hapus Data')
  print('3. Tampilkan Data')
  print('4. Selesai')
  pilihan = input('Masukkan Pilihanmu (1, 2, 3, atau 4): ')
  return pilihan

def tambah(array, limit):
  reconfirm = True
  while reconfirm:
    item = input(f'Masukkan data pada indeks ke-{size + 1}: ')
    if item:
      if item in array:
        print("* Peringatan *")
        print(f'Data {item} sudah berada di dalam antrian. Mohon masukkan data yang berbeda')
      else:
        array.append(item)
        print("* Info *")
        print(f'Data {item} berhasil masuk ke dalam antrian\n')
        reconfirm = False
    else:
      print("* Peringatan *")
      print('Data yang ingin ditambahkan tidak boleh kosong\n')
      reconfirm = False

def hapus(array):
  reconfirm = True
  while reconfirm:
    if sizearray(array) > 0:
      item = input('Data yang ingin dihapus: ')
      if item:
        if item in array:
          removeItem(array, item)
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

def tampil(array):
  print('Isi Antrian: ')
  size = sizearray(array)
  if size != 0:
    i = 0
    while i < size:
      if i != size - 1:
        print(array[i], end=" - ")
      else:
        print(array[i])
      i+=1
  else:
    print('* Peringatan *')
    print('Antrian kosong, lakukan tambah data terlebih dahulu')
  print()

def main():
  print("""
=====================================================================
------------------------ Selamat Datang -----------------------------
--- Program Menambah, Menghapus, dan Menampilkan Data (Arraylist) ---
=====================================================================
""")
  array = createArray()
  limit = input('Masukkan limit antrian: ')
  lanjut = True
  while lanjut:
    pilihan = pilihMenu()
    if pilihan == '1': # Tambah Data
      tambah(array, limit)
    elif pilihan == '2': # Hapus Data
      hapus(array)
    elif pilihan == '3': # Tampil Data
      tampil(array)
    elif pilihan == '4': # Program Selesai
      lanjut = False
      print('Program diakhiri. Sekian, terima kasih.\n')
    else:
      print("* Peringatan *")
      print('Harap memilih pilihan yang tersedia!\n')
main()
