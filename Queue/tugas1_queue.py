# Queue Tugas1 Kelompok 3
# 1. AKMAL RAFI DIARA PUTRA            - 1313621007
# 2. MUHAMMAD AQMAL KHAFIDZ PRATAMA    - 1313621005
# 3. RAWDO MADINA                      - 1313621028
# 4. RADEN RORO ZIVA AZZAHRAH KHALILA  - 1313621034
# 5. SALWA TSABITAH                    - 1313621042

def createArray():
  arr = []
  return arr

def addItem(arr, item):
  arr.append(item)

def removeItem(arr):
  return arr.pop(0)

def sizeArray(arr):
  return len(arr)

def isNum(item):
  if item.isnumeric():
    return True
  else:
    print("* Peringatan *")
    print("Mohon masukkan dalam bentuk angka.\n")
    return False

def main():
  cobaLagi = True
  while cobaLagi:
    print("""
============================================================
-------------------- Selamat Datang ------------------------
----------- Program Antrian Pendaftaran Membership ---------
============================================================
""")

    reconfirm = True
    while reconfirm:
      jmlMaksimal = input('Masukkan maksimum panjang antrian pendaftar yang dapat dilayani hari ini (dalam bentuk angka): ')
      if isNum(jmlMaksimal):
        break

    reconfirm = True
    while reconfirm:
      jmlKedatangan = input('Masukkan banyaknya kedatangan pendaftar hari ini (dalam bentuk angka): ')
      if isNum(jmlKedatangan):
        break

    jmlMaksimal = int(jmlMaksimal)
    jmlKedatangan = int(jmlKedatangan)
    arr = createArray()

    print('\nUntuk para pendaftar, diharapkan mengisi daftar kehadiran')
    i = 0
    while i < jmlKedatangan:
      nama = input('Masukkan Nama pendaftar: ')
      if nama:
        addItem(arr, nama)
        if sizeArray(arr) > jmlMaksimal:
          print("* Peringatan *")
          print(f'Antrian Penuh! Pendaftar atas nama {nama} tidak dapat dimasukkan, harap datang dihari berikutnya\n')
        else:
          print(f'Pendaftar atas nama {nama} berhasil mendaftar Membership\n')
        i+=1
      else:
        print("* Peringatan *")
        print('Nama Tidak Boleh Kosong\n')
        
    print(f'Para pendaftar yang dapat dilayani hari ini:')
    i = 0
    while i < jmlMaksimal:
      if sizeArray(arr) == 0:
        break
      else:
        print(f'{i + 1}. {removeItem(arr)}')
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
      elif konfirmasi == '2':
        print('Program diakhiri. Sekian, terima kasih.\n')
        reconfirm = cobaLagi = False
      else:
        print('* Peringatan *')
        print('Mohon ketik dengan pilihan yang tersedia.')
main()