import time

def bubbleSort(arr):
  n = len(arr)
  print(f'array: {arr}')
  for i in range(n):
    swapping = False
    for j in range(0, n - i - 1):
      print(f'step = {i+1}, i = {j}')
      print(f'Apakah {arr[j]} > {arr[j + 1]} ?')

      if arr[j] > arr[j + 1] :
        temp = arr[j]
        arr[j] = arr[j + 1]
        arr[j + 1] = temp
        swapping = True
        time.sleep(0.2)
        print(f'Ya, maka tukar {arr[j]} dengan {arr[j + 1]} => {arr}')
      else:
        print(f'Tidak, maka tidak melakukan pertukaran')
      print()

    if not swapping:
      break
  return arr

def rev_bubbleSort(arr):
  n = len(arr)
  print(f'array: {arr}')
  for i in range(n): # loop setiap elemen array
    swapping = False
    for j in range(0, n - i - 1): # loop untuk bandingkan elemen array
      print(f'step = {i+1}, i = {j}')
      print(f'Apakah {arr[j]} < {arr[j + 1]} ?')

      if arr[j] < arr[j + 1] :
        temp = arr[j]
        arr[j] = arr[j + 1]
        arr[j + 1] = temp
        swapping = True
        time.sleep(0.2)
        print(f'Ya, maka tukar {arr[j]} dengan {arr[j + 1]} => {arr}')
      else:
        print(f'Tidak, maka tidak melakukan pertukaran')
      print()
      
    if not swapping:
      break
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
    store_1 = []
    store_2 = []
    for i in range(len(data)):
      new_data.append(int(data[i]))
      store_1.append(int(data[i]))
      store_2.append(int(data[i]))
# -2, 45, 0, 11, -9
    clear = True
    while clear:
      aksi = pilihAksi()
      if aksi == "1":
        bubbleSort(store_1)
        print('Hasil pengurutan keatas: ')
        for i in range(len(store_1)):
          if i != len(store_1) - 1:
            print(store_1[i], end=", ")
          else:
            print(store_1[i])
      
      elif aksi == "2":
        rev_bubbleSort(store_2)
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