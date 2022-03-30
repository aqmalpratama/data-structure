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
    print('\n--------- Program Input Nama Secara Dinamis --------------')
    maksimal = input('Masukkan maksimal jumlah mahasiswa yang dapat ditampung pada matkul SDA: ')
    if maksimal:
      maksimal = int(maksimal)
      if maksimal > 0:
        for i in range(maksimal):
          nama = input(f'Masukkan nama mahasiswa ke-{i+1} : ')
          push(mahasiswa, nama)

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
        print('Jumlah maksimal mahasiswa tidak boleh bernilai 0.')
    else:
      print('* Peringatan *')
      print('Jumlah maksimal mahasiswa tidak boleh kosong.')

main()
    