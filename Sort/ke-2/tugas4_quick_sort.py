def quickSort(array, low, high):
  if low < high:
    pi = partition(array, low, high)
    quickSort(array, low, pi - 1)
    quickSort(array, pi + 1, high)

def partition(array, low, high):
  pivot = array[high]
  i = low - 1
  for j in range(low, high):
    if array[j] <= pivot:
      i += 1
      array[i], array[j] = array[j], array[i]
  array[i + 1], array[high] = array[high], array[i + 1]
  return i + 1
  
def main():
  ingin_lanjut = True
  while ingin_lanjut:
    print('------ Program Quick Sort ------\n')
    print('* CATATAN *')
    print('Mohon masukkan angka dengan tanda koma sebagai pemisah. Jika dirasa sudah cukup, maka tekan enter untuk melakukan proses pengurutan angka.')
    print('Contoh memasukkan angka : 21, 32, 17, 2, 51')
    angka = input('Masukkan beberapa angka acak yang akan diurutkan: ')
    data = angka.split(", ")
    new_data = []
    for i in range(len(data)):
      new_data.append(int(data[i]))

    quickSort(new_data, 0, len(data) - 1)
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