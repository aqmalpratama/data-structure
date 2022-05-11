import time
def insertionSort(array):
  for i in range(1, len(array)):
    key = array[i]
    j = i - 1
    while j >= 0 and key < array[j]:
      time.sleep(0.2)
      print(array)
      array[j + 1] = array[j]
      j -= 1
    array[j + 1] = key
  return array

def rev_insertionSort(array):
  for i in range(1, len(array)):
    key = array[i]
    j = i - 1
    while j >= 0 and key > array[j]:
      time.sleep(0.2)
      print(array)
      array[j + 1] = array[j]
      j -= 1
    array[j + 1] = key
  return array

def pilihAksi():
  print("Daftar Aksi:\n 1. Mengurutkan Keatas\n 2. Mengurutkan Kebawah\n 3. Keluar")
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
    data = angka.split(", ")
    new_data = []
    for i in range(len(data)):
      new_data.append(int(data[i]))
    clear = True
    while clear:
      aksi = pilihAksi()
      if aksi == "1":
        insertionSort(new_data)
        print('Hasil pengurutan keatas: ')
        for i in range(len(new_data)):
          if i != len(new_data) - 1:
            print(new_data[i], end=", ")
          else:
            print(new_data[i])
      elif aksi == "2":
        rev_insertionSort(new_data)
        print('Hasil pengurutan kebawah: ')
        for i in range(len(new_data)):
          if i != len(new_data) - 1:
            print(new_data[i], end=", ")
          else:
            print(new_data[i])
      elif aksi == "3":
        clear = False
      else:
        print("Pilihan tidak valid\n")
    try_again = input("Ingin menjalankan program kembali? (Y/N): ").upper
    if try_again == "N":
      state_try = False
      
main()