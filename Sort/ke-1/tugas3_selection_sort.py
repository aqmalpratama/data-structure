import time
def selectionSort(array):
  print(f'Array awal: {array}')
  for i in range(len(array)):
    min_index = i
    swapping = False
    print(f'first minimum: {array[min_index]}')
    for j in range(i + 1, len(array)):
      print(f'Apakah {array[j]} < {array[min_index]} ?')
      if array[j] < array[min_index]:
        min_index = j
        swapping = True
        print(f'Ya, maka nilai minimum sekarang: {array[min_index]}')
      else:
        print(f'Tidak, maka nilai minimum tidak berubah: {array[min_index]}')
    array[i], array[min_index] = array[min_index], array[i]
    if swapping:
      print(f'tukar {array[i]} dengan {array[min_index]} => {array}')
    else:
      print(f'Tidak ada yang ditukar, maka {array}')
    print()
  return array

def rev_selectionSort(array):
  print(f'Array awal: {array}')
  for i in range(len(array)):
    min_index = i
    swapping = False
    print(f'first minimum: {array[min_index]}')
    for j in range(i + 1, len(array)):
      print(f'Apakah {array[j]} > {array[min_index]} ?')
      if array[j] > array[min_index]:
        min_index = j
        swapping = True
        print(f'Ya, maka nilai minimum sekarang: {array[min_index]}')
      else:
        print(f'Tidak, maka nilai minimum tidak berubah: {array[min_index]}')
    array[i], array[min_index] = array[min_index], array[i]
    if swapping:
      print(f'tukar {array[i]} dengan {array[min_index]} => {array}')
    else:
      print(f'Tidak ada yang ditukar, maka {array}')
    print()
  return array

def pilihAksi():
  print("\nDaftar Aksi:\n 1. Mengurutkan Keatas\n 2. Mengurutkan Kebawah\n 3. Keluar")
  pilihan = input("Masukkan pilihan Anda (1, 2, atau 3): ")
  return pilihan

def main():
  print('------ Program Selection Sort ------')
  print('* CATATAN *')
  print('Mohon masukkan angka dengan tanda koma sebagai pemisah.\nJika dirasa sudah cukup, maka tekan enter untuk melakukan proses pengurutan angka.')
  print('Contoh memasukkan angka : 21, 32, 17, 2, 51')
  state_try = True
  while state_try:
    angka = input('Masukkan beberapa angka acak yang akan diurutkan: ')
    # 20, 12, 10, 15, 2
    data = angka.split(", ")
    new_data = []
    store_1 = []
    store_2 = []
    for i in range(len(data)):
      new_data.append(int(data[i]))
      store_1.append(int(data[i]))
      store_2.append(int(data[i]))
    clear = True
    while clear:
      aksi = pilihAksi()
      if aksi == "1":
        print(f'\nProses pengurutan ke atas....')
        selectionSort(store_1)
        print('Hasil pengurutan keatas: ')
        for i in range(len(store_1)):
          if i != len(store_1) - 1:
            print(store_1[i], end=", ")
          else:
            print(store_1[i])
      elif aksi == "2":
        rev_selectionSort(store_2)
        print('Hasil pengurutan kebawah: ')
        for i in range(len(store_2)):
          if i != len(store_2) - 1:
            print(store_2[i], end=", ")
          else:
            print(store_2[i])
      elif aksi == "3":
        clear = False
      else:
        print("Pilihan tidak valid\n")
    try_again = input("Ingin menjalankan program kembali? (Y/N): ")
    if try_again.upper() == "N":
      state_try = False
      print("Terima kasih sudah menggunakan program ini.")

main()