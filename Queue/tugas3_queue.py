def createArray():
  array = list()
  return array

def addItemToArray(array, item):
  array.append(item)

def removeItemFromArray(array, item = ''):
  if item:
    return array.remove(item)
  else:
    return array.pop(0)

def sizeArray(array):
  return len(array)

def pilihMenu():
  print('Menu:')
  print('1. Tambah Data')
  print('2. Hapus Data')
  print('3. Tampilkan Data')
  print('4. Kosongkan Antrian')
  print('5. Selesai')
  pilihan = input('Masukkan Pilihanmu (1, 2, 3, atau 4 lalu tekan Enter): ')
  return pilihan

def tambah(array, limit):
  size = sizeArray(array)
  if size == int(limit):
    print("* Peringatan *")
    print('Antrian sudah penuh !!\n')
  else:
    reconfirm = True
    while reconfirm:
      item = input(f'Masukkan data ke-{size + 1}: ')
      if item:
        if item in array:
          print("* Peringatan *")
          print(f'Data {item} sudah berada di dalam antrian. Mohon masukkan data yang berbeda')
        else:
          addItemToArray(array, item)
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
    if sizeArray(array) > 0:
      item = input('Data yang ingin dihapus: ')
      if item:
        if item in array:
          removeItemFromArray(array, item)
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
  size = sizeArray(array)
  array.sort()
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
  print()
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
print("""---   TUGAS 2 NO 3 - IMPLEMENTASI ANTRIAN DENGAN KELAS ARRAYLIST   ---""")
print("ANGGOTA KELOMPOK 3: ")
print("1. AKMAL RAFI DIARA PUTRA            - 1313621007") 
print("2. MUHAMMAD AQMAL KHAFIDZ PRATAMA    - 1313621005") 
print("3. RAWDO MADINA                      - 1313621028") 
print("4. RADEN RORO ZIVA AZZAHRAH KHALILA  - 1313621034") 
print("5. SALWA TSABITAH                    - 1313621042") 
main()
