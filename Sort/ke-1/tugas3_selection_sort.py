def selectionSort(array):
  for i in range(len(array)):
    min_index = i
    for j in range(i + 1, len(array)):
      if array[j] < array[min_index]:
        min_index = j
    array[i], array[min_index] = array[min_index], array[i]
  return array

def main():
  ingin_lanjut = True
  while ingin_lanjut:
    print('------ Program Bubble Sort ------\n')
    print('* CATATAN *')
    print('Mohon masukkan angka dengan tanda koma sebagai pemisah. Jika dirasa sudah cukup, maka tekan enter untuk melakukan proses pengurutan angka.')
    print('Contoh memasukkan angka : 21, 32, 17, 2, 51')
    angka = input('Masukkan beberapa angka acak yang akan diurutkan: ')
    data = angka.split(", ")
    new_data = []
    for i in range(len(data)):
      new_data.append(int(data[i]))

    insertionSort(new_data)
    print('Hasil: ')
    for i in range(len(new_data)):
      if i != len(new_data) - 1:
        print(new_data[i], end=", ")
      else:
        print(new_data[i])

    print('\n--- Pilihan ---')
    print('1. Program akan dijalankan kembali')
    print('2. Program akan diakhiri')
    konfirmasi = True
    while konfirmasi:
      konfirmasi = input("Apakah Anda ingin menjalankan program ini kembali? (ketik 1 atau 2): ")
      if konfirmasi == '1':
        print("Baik, program dijalankan kembali\n")
        konfirmasi = False
      elif konfirmasi == '2':
        print('Program diakhiri. Sekian, terima kasih\n')
        konfirmasi = ingin_lanjut = False
      else:
        print('* Peringatan *')
        print('Pilihan tidak valid\n')
main()