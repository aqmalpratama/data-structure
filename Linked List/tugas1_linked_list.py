def tampil(data):
  if bool(data.items()) == False:
    print('Data kosong')
    print('Mohon tambah data terlebih dahulu')
  else:
    for simpul_id, simpul_info in data.items():
      print("\nId Mahasiswa:", simpul_id)
      print(simpul_info['kode'] + ' : ' +  simpul_info['nama'])
  print()

def tambah(data):
  if bool(data.items()) == False:
    nextSimpul = 'simpul_1'
  else:
    last_key = list(data.keys())[-1]
    explode = last_key.split("_")
    nextSimpul = explode[0] + '_' + str(int(explode[1]) + 1)

  kode = input('Masukkan kode: ')
  nama = input('Masukkan nama: ')
  data[nextSimpul] = {}
  data[nextSimpul]['kode'] = kode.upper()
  data[nextSimpul]['nama'] = nama
  print(f'Berhasil menambahkan data dengan kode {kode.upper()} dan nama {nama}')
  print()

def temukan(data):
  if bool(data.items()) == False:
    print('Data kosong')
    print('Mohon tambah data terlebih dahulu')
  else:
    reconfirm = True
    while reconfirm:
      search_filter = input('Anda ingin menemukan data berdasarkan apa (kode atau nama): ')
      search_key = input(f'Masukkan data yang Anda inginkan untuk dihapus berdasarkan {search_filter}: ')
      reconfirm = False

    exist = False
    for simpul_id, simpul_info in data.items():
      if (search_filter == 'kode' and simpul_info['kode'] == search_key) or (search_filter == 'nama' and simpul_info['nama'] == search_key):
        simpul_ke = simpul_id
        kode      = simpul_info['kode']
        nama      = simpul_info['nama']
        exist     = True
      
    print(f'Pencarian {search_key}')
    print('Hasil Pencarian:')
    if exist:
      print(kode + ' : ' +  nama)
    else:
      print(search_key + ' tidak ditemukan')
  print()

def hapus(data):
  if bool(data.items()) == False:
    print('Data kosong')
    print('Mohon tambah data terlebih dahulu')
  else:
    ingin_hapus = True
    while ingin_hapus:
      search_filter = input('Anda ingin menghapus data berdasarkan apa (kode atau nama): ')
      if search_filter != 'kode' and search_filter != 'nama':
        print('Pilihan tidak tersedia')
      else:
        search_key = input(f'Masukkan data yang Anda inginkan untuk dihapus berdasarkan {search_filter}: ')
        reconfirm = False

    exist = False
    for simpul_id, simpul_info in data.items():
      if search_filter == 'kode' and simpul_info['kode'] == search_key:
        simpul_ke = simpul_id
        nama      = simpul_info['nama']
        exist     = True
      if search_filter == 'nama' and simpul_info['nama'] == search_key:
        simpul_ke = simpul_id
        kode      = simpul_info['kode']
        exist     = True
    
    if exist == True:
      data.pop(simpul_ke)
      print(f'Berhasil menghapus data {search_key}')
    else:
      print('Data tidak ditemukan')
  print()

def pilihMenu():
  print('Menu:')
  print('1. Tambah Data')
  print('2. Hapus Data')
  print('3. Temukan Data')
  print('4. Tampilkan Data')
  print('5. Selesai')
  pilihan = input('Masukkan Pilihanmu (1, 2, 3, 4, atau 5): ')
  return pilihan

def main():
  print('---- Program CRUD (LINKED LIST) ----')
  dictionary_mahasiswa = {
    'simpul_1' : {
      'kode'  : 'AZL',
      'nama'  : 'Azrila'
    },
    'simpul_2' : {
      'kode'  : 'AQM',
      'nama'  : 'Aqmal'
    },
    'simpul_3' : {
      'kode'  : 'SKR',
      'nama'  : 'Sekar'
    },
    'simpul_4' : {
      'kode'  : 'CCP',
      'nama'  : 'Cecep'
    },
  }

  selesai = False
  while selesai == False:
    pilihan = pilihMenu()
    if pilihan == '1': # Tambah Data
      tambah(dictionary_mahasiswa)
    elif pilihan == '2': # Hapus Data
      hapus(dictionary_mahasiswa)
    elif pilihan == '3': # Temukan Data
      temukan(dictionary_mahasiswa)
    elif pilihan == '4': # Tampil Data
      tampil(dictionary_mahasiswa)
    elif pilihan == '5': # Program Selesai
      selesai = True
      print('Program diakhiri. Sekian, terima kasih.\n')
    else:
      print('Pilihan tidak tersedia. Harap memilih pilihan yang tersedia!\n')

main()