def main():
  cobaLagi = True
  while cobaLagi:
    print('\n---------- Program Antrian (Queue) Membership ----------')

    reconfirm = True
    while reconfirm:
      jmlMaksimal = input('Masukkan Maksimum Panjang Antrian (dalam bentuk angka): ')
      if jmlMaksimal.isnumeric():
        reconfirm = False
      else:
        print("Mohon masukkan dalam bentuk angka.\n")
        reconfirm = True

    reconfirm = True
    while reconfirm:
      jmlKedatangan = input('Masukkan Banyaknya Kedatangan Pelanggan Hari Ini (dalam bentuk angka): ')
      if jmlKedatangan.isnumeric():
        reconfirm = False
      else:
        print("Mohon masukkan dalam bentuk angka.\n")
        reconfirm = True

    jmlMaksimal = int(jmlMaksimal)
    jmlKedatangan = int(jmlKedatangan)
    queue = []

    print('\n--- Menu ---')
    print('1. Tambah Data\n2. Tampilkan Data\n')

    menu = input('Masukkan Pilihan Anda (1 atau 2): ')

    if menu == '1':
      print('\nUntuk Pelanggan, Diharapkan mengisi daftar kehadiran')
      i = 0
      while i < jmlKedatangan:
        nama = input('Masukkan Nama Pelanggan: ')
        if nama:
          queue.append(nama)
          if len(queue) > jmlMaksimal:
            print('Antrian Penuh!')
            print(f'Pelanggan atas nama {nama} tidak dapat dimasukkan, harap datang dihari berikutnya\n')
          else:
            print(f'Pelanggan atas nama {nama} berhasil mendaftar Membership\n')
          i+=1
        else:
          print('Nama Tidak Boleh Kosong')
    elif menu == '2':
      print(f'Isi Antrian:')
      i = 0
      while i < jmlMaksimal:
        if len(queue) == 0:
          break
        else:
          print(f'{i + 1}. {queue.pop(0)}')
        i+=1

    reconfirm = True
    while reconfirm:
      print('\n--- Pilihan ---')
      print('1. Program akan dijalankan kembali')
      print('2. Program akan diakhiri')
      konfirmasi = input("Apakah Anda ingin menjalankan program ini kembali? (ketik 1 atau 2): ")
      if konfirmasi == '1':
        print("Baik, program dijalankan kembali.\n")
        reconfirm = False
        cobaLagi = True
      elif konfirmasi == '2':
        print('Program diakhiri. Sekian, terima kasih.\n')
        reconfirm = cobaLagi = False
      else:
        print('* Peringatan *')
        print(f'Mohon maaf, pilihan {konfirmasi} tidak tersedia.')
        print('Mohon ketik dengan pilihan yang tersedia.')
        reconfirm = True

main()