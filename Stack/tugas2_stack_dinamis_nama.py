def createStack():
  stack = []
  return stack

def size(stack):
  return len(stack)

def isEmpty(stack):
  if size(stack) == 0:
    return True

def clear(stack):
  return stack.clear()

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
    print('--- Program Input Nama Secara Dinamis ---')
    maksimal = int(input('Masukkan maksimal jumlah mahasiswa baru yang dapat mendaftar kelas matkul SDA: '))

    if maksimal > 0:
      print(f'\nKelas matkul SDA menampung sebanyak {maksimal} mahasiswa')
      for i in range(maksimal):
        nama = input(f'Masukkan nama mahasiswa ke-{i+1}: ')
        if nama:
          push(mahasiswa, nama)
        else:
          print('* Peringatan *')
          print(f'Nama tidak boleh kosong')          
        
      print('Ternyata ada mahasiswa telat yang ingin mendaftar kelas matkul SDA')
      nama = input('Masukkan nama mahasiswa: ')

      if len(mahasiswa) == maksimal:
        print('* Peringatan *')
        print(f'Kelas penuh! {nama} tidak dapat mendaftar')

      print(f"\nDaftar mahasiswa pada matkul SDA: ")
      for i in range(maksimal):
        print(f'Nama mahasiswa ke-{i+1} : {pop(mahasiswa)}')

      reconfirm = True
      while reconfirm == True:
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

    else:
      print('* Peringatan *')
      print('Jumlah maksimal mahasiswa tidak boleh kosong.')

main()
    