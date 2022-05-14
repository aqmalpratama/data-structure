def createStack():
  stack = []
  return stack

def size(stack):
  return len(stack)

def isEmpty(stack):
  if size(stack) == 0:
    return True

def push(stack, item):
  stack.append(item)

def pop(stack):
  if isEmpty(stack):
    return 'Error'
  else:
    return stack.pop()

def main():
  mahasiswa = createStack()
  cobaLagi = True
  while cobaLagi == True:
    print()
    maksimal = input('Masukkan maksimal jumlah mahasiswa yang dapat ditampung pada matkul SDA: ')
    if bool(maksimal) == False:
      print('Input harus diisi')
      main()
    
    if int(maksimal) <= 0:
      print('Input harus lebih dari 0')
      main()
    
    if bool(maksimal) == True and int(maksimal) > 0:
      maksimal = int(maksimal)
      # for i in range(maksimal):
      #   nama = input(f'Masukkan nama mahasiswa ke-{i+1} : ')
      #   push(mahasiswa, nama)
      nomor = 0
      while nomor < maksimal:
        nama = input(f'Masukkan nama mahasiswa ke-{nomor + 1} : ')
        if bool(nama) == False:
          print('Input harus diisi')
        else:
          push(mahasiswa, nama)
          nomor += 1
      print(f"\nDaftar mahasiswa pada matkul SDA: ")
      for i in range(maksimal):
        print(f'Nama mahasiswa ke-{i+1} : {pop(mahasiswa)}')
        
      reconfirm = True
      while reconfirm:
        print('\n--- Pilihan ---')
        print('1. Program akan dijalankan kembali')
        print('2. Program akan diakhiri')
        konfirmasi = input("Apakah Anda ingin menjalankan program ini kembali? (Pilih 1 atau 2 lalu tekan Enter): ")
        if konfirmasi == '1':
          print("Baik, program dijalankan kembali.\n")
          reconfirm = False
        elif konfirmasi == '2':
          print('Program diakhiri. Sekian, terima kasih.\n')
          exit()
        else:
          print('* Peringatan *')
          print('Pilihan tidak valid')

print()
print("""--- TUGAS 1 NO 3 - IMPLEMENTASI INPUT DINAMIS NAMA DENGAN STACK ---""")
print("ANGGOTA KELOMPOK 3: ")
print("1. AKMAL RAFI DIARA PUTRA            - 1313621007") 
print("2. MUHAMMAD AQMAL KHAFIDZ PRATAMA    - 1313621005") 
print("3. RAWDO MADINA                      - 1313621028") 
print("4. RADEN RORO ZIVA AZZAHRAH KHALILA  - 1313621034") 
print("5. SALWA TSABITAH                    - 1313621042") 
main()
    