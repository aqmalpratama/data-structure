def tampil(data):
  if bool(data.items()) == False:
    print('---------- INFO ------------')
    print('Data kosong')
    print('Mohon tambah data terlebih dahulu')
  else:
    for m_id, m_info in data.items():
      print("\nId Mahasiswa:", m_id)
      print(m_info['kode'] + ' : ' +  m_info['nama'])
  print()

def tambah(data, next_id):
  kode = input('Masukkan kode: ')
  nama = input('Masukkan nama: ')
  data[next_id] = {}
  data[next_id]['kode'] = kode.upper()
  data[next_id]['nama'] = nama
  print(f'Berhasil menambahkan data dengan kode {kode.upper()} dan nama {nama}')
  print()
  return next_id

def temukan(data):
  if bool(data.items()) == False:
    print('---------- INFO ------------')
    print('Data kosong')
    print('Mohon tambah data terlebih dahulu')
  else:
    search_filter = input('Anda ingin menemukan data berdasarkan apa (kode atau nama): ')
    search_key = input(f'Masukkan data yang Anda inginkan untuk dihapus berdasarkan {search_filter}: ')

    exist = False
    for m_id, m_info in data.items():
      if (search_filter == 'kode' and m_info['kode'].lower() == search_key) or (search_filter == 'nama' and m_info['nama'].lower() == search_key):
        kode      = m_info['kode']
        nama      = m_info['nama']
        exist     = True
    
    print('---------- INFO ------------')
    print(f'Pencarian {search_key}')
    print('Hasil Pencarian:')
    if exist:
      print(kode + ' : ' +  nama)
    else:
      print(search_key + ' tidak ditemukan')
  print()

def hapus(data):
  if bool(data.items()) == False:
    print('---------- INFO ------------')
    print('Data kosong')
    print('Mohon tambah data terlebih dahulu')
  else:
    search_filter = input('Anda ingin menghapus data berdasarkan apa (kode atau nama): ')
    search_key = input(f'Masukkan data yang Anda inginkan untuk dihapus berdasarkan {search_filter}: ')

    exist = False
    for m_id, m_info in data.items():
      if (search_filter == 'kode' and m_info['kode'].lower() == search_key) or (search_filter == 'nama' and m_info['nama'].lower() == search_key):
        id_ke     = m_id
        kode      = m_info['kode']
        nama      = m_info['nama']
        exist     = True
    
    print('---------- INFO ------------')
    if exist == True:
      data.pop(id_ke)
      print(f'Berhasil menghapus data {search_key}')
    else:
      print('Data tidak ditemukan')
  print()
  return id_ke

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
    # 1 : {
    #   'kode'  : 'AZL',
    #   'nama'  : 'Azrila'
    # },
    # 2 : {
    #   'kode'  : 'AQM',
    #   'nama'  : 'Aqmal'
    # },
    # 3 : {
    #   'kode'  : 'SKR',
    #   'nama'  : 'Sekar'
    # },
    # 4 : {
    #   'kode'  : 'CCP',
    #   'nama'  : 'Cecep'
    # },
  }

  next_id = 0
  selesai = False
  while selesai == False:
    pilihan = pilihMenu()
    if pilihan == '1': # Tambah Data
      if bool(dictionary_mahasiswa.items()) == False:
        next_id = 1
      else:
        next_id += 1
      next_id = tambah(dictionary_mahasiswa, next_id)
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