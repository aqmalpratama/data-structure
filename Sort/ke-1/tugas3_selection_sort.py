def selectionSort(array, size):
  for step in range(size):
    min_idx = step

    for i in range(step + 1, size):
      # to sort in descending order, change > to < in this line
      # select the minimum element in each loop
      if array[i] < array[min_idx]:
        min_idx = i
      
    # put min at the correct position
    (array[step], array[min_idx]) = (array[min_idx], array[step])

# data = [-2, 45, 0, 11, -9]
ingin_lanjut = True
while ingin_lanjut:
  print('------ Program Selection Sort ------')
  print('* CATATAN *')
  print('Mohon masukkan angka dengan tanda koma sebagai pemisah. Jika dirasa sudah cukup, maka tekan enter untuk melakukan proses pengurutan angka.')
  print('Contoh memasukkan angka : 21, 32, 17, 2, 51')
  angka = input('Masukkan beberapa angka acak yang akan diurutkan: ')
  data = angka.split(", ")
  new_data = []
  for i in range(len(data)):
    new_data.append(int(data[i]))

  selectionSort(new_data, len(new_data))
  print('Hasil: ')
  for i in range(len(new_data)):
    if i != len(new_data) - 1:
      print(new_data[i], end=", ")
    else:
      print(new_data[i])

  print('\n--- Pilihan ---')
  print('1. Program akan dijalankan kembali')
  print('2. Program akan diakhiri')
  konfirmasi_lanjut = True
  while konfirmasi_lanjut:
    konfirmasi = input("Apakah Anda ingin menjalankan program ini kembali? (ketik 1 atau 2): ")
    if konfirmasi == '1':
      print("Baik, program dijalankan kembali\n")
      konfirmasi_lanjut = False
    elif konfirmasi == '2':
      print('Program diakhiri. Sekian, terima kasih\n')
      konfirmasi_lanjut = ingin_lanjut = False
    else:
      print('* Peringatan *')
      print(f'Mohon maaf, pilihan {konfirmasi} tidak tersedia')
      print('Mohon ketik dengan pilihan yang tersedia\n')
      konfirmasi_lanjut = True
  
# bubbleSort(data)
# print('Sorted Array in Ascending Order:')
# print(data)