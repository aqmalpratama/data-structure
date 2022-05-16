import time
# Optimized Bubble sort in Python
def bubbleSort(arr):
  n = len(arr)
  for i in range(n):
    for j in range(0, n - i - 1):
      if arr[j] > arr[j + 1] :
        temp = arr[j]
        arr[j] = arr[j + 1]
        arr[j + 1] = temp

        time.sleep(0.2)
        print(f'Tukar {arr[j]} dengan {arr[j + 1]} => {arr}')
  return arr

def rev_bubbleSort(arr):
  n = len(arr)
  for i in range(n):
    for j in range(0, n - i - 1):
      if arr[j] < arr[j + 1] :
        temp = arr[j]
        arr[j] = arr[j + 1]
        arr[j + 1] = temp

        time.sleep(0.2)
        print(f'Tukar {arr[j]} dengan {arr[j + 1]} => {arr}')
  return arr

def pilihAksi():
  print("\nDaftar Aksi:\n 1. Mengurutkan Keatas\n 2. Mengurutkan Kebawah\n 3. Keluar")
  pilihan = input("Masukkan pilihan Anda (1, 2, atau 3): ")
  return pilihan

def main():
  print('------ Program Bubble Sort ------')
  print('* CATATAN *')
  print('Mohon masukkan angka dengan tanda koma sebagai pemisah.\nJika dirasa sudah cukup, maka tekan enter untuk melakukan proses pengurutan angka.')
  print('Contoh memasukkan angka : 25, 57, 48, 39, 18, 95, 80, 35')
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
        bubbleSort(new_data)
        print('\nHasil pengurutan keatas: ')
        for i in range(len(new_data)):
          if i != len(new_data) - 1:
            print(new_data[i], end=", ")
          else:
            print(new_data[i])
      
      elif aksi == "2":
        rev_bubbleSort(new_data)
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
    try_again = input("Ingin menjalankan program kembali? (Y/N): ")
    if try_again.upper() == "N":
      state_try = False
      print("Terima kasih sudah menggunakan program ini.")
      
main()