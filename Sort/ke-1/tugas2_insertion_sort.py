import time
def insertionSort(array):
  print('Proses pengurutan ke atas: ')
  for i in range(1, len(array)):
    key = array[i]
    j = i - 1

    print(f'key: {key}')
    print(array)
    while j >= 0 and key < array[j]:
      time.sleep(0.2)
      array[j + 1] = array[j]
      temp = array[j + 1]
      print(array)
      j -= 1
    array[j + 1] = key
    print(f'Pindahkan {array[j + 1]} setelah {array[j]} => {array}\n')
  return array

def rev_insertionSort(array):
  print('Proses pengurutan ke bawah: ')
  for i in range(1, len(array)):
    key = array[i]
    j = i - 1
    print(f'key: {key}')
    print(array)
    while j >= 0 and key > array[j]:
      time.sleep(0.2)
      array[j + 1] = array[j]
      temp = array[j + 1]
      print(array)
      j -= 1
    array[j + 1] = key
    print(f'Pindahkan {array[j + 1]} setelah {array[j]} => {array}\n')
  return array

def pilihAksi():
  print("\nDaftar Aksi:\n 1. Mengurutkan Ke atas\n 2. Mengurutkan Ke bawah\n 3. Keluar")
  pilihan = input("Masukkan pilihan Anda (1, 2, atau 3): ")
  return pilihan

def main():
  print('------ Program Insertion Sort ------')
  print('* CATATAN *')
  print('Mohon masukkan angka dengan tanda koma sebagai pemisah.\nJika dirasa sudah cukup, maka tekan enter untuk melakukan proses pengurutan angka.')
  print('Contoh memasukkan angka : 21, 32, 17, 2, 51')
  state_try = True
  while state_try:
    angka = input('Masukkan beberapa angka acak yang akan diurutkan: ')
    # 9, 5, 1, 4, 3
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
        insertionSort(store_1)
        print('Hasil pengurutan keatas: ')
        for i in range(len(store_1)):
          if i != len(store_1) - 1:
            print(store_1[i], end=", ")
          else:
            print(store_1[i])
      elif aksi == "2":
        rev_insertionSort(store_2)
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