def quickSort(array, low, high):
  if low < high:
    pi = partition(array, low, high)
    quickSort(array, low, pi - 1)
    quickSort(array, pi + 1, high)
  # print(array)

def partition(array, low, high):
  pivot = array[high]
  print("\nPivot: ", pivot)
  print(array)
  i = low - 1
  for j in range(low, high):
    if array[j] <= pivot:
      i += 1
      array[i], array[j] = array[j], array[i]
      print(f'Cek: {array[i]} Lebih kecil dari {pivot} dan {array[j]} | Sel Tujuan: {array[j]}')
      print(array)
      # print(f'swapping element at i: {array[i]} with element at j:{array[j]} => {array}')
  array[i + 1], array[high] = array[high], array[i + 1]
  print(f'Menukar pivot: {array[i + 1]} dengan data yang lebih besar yang ditentukan oleh i: {array[high]} => {array}')
  return i + 1

def rev_quickSort(array, low, high):
  if low < high:
    pi = rev_partition(array, low, high)
    rev_quickSort(array, low, pi - 1)
    rev_quickSort(array, pi + 1, high)

def rev_partition(array, low, high):
  pivot = array[high]
  print("\nPivot: ", pivot)
  print(array)
  i = low - 1
  for j in range(low, high):
    if array[j] >= pivot:
      i += 1
      array[i], array[j] = array[j], array[i]
      print(f'Cek: {array[i]} lebih besar dari {pivot} dan {array[j]} | Sel Tujuan: {array[j]}')
      print(array)
  array[i + 1], array[high] = array[high], array[i + 1]
  print(f'Menukar pivot: {array[i + 1]} dengan data yang lebih besar yang ditentukan oleh i: {array[high]} => {array}')
  return i + 1
  
def pilihAksi():
  print("\nDaftar Aksi:\n 1. Mengurutkan Keatas\n 2. Mengurutkan Kebawah\n 3. Perbarui Data\n 4. Keluar")
  pilihan = input("Masukkan pilihan Anda (1, 2, 3, atau 4): ")
  return pilihan

def input_data():
  while True:
      try:
        # 8 7 6 1 0 9 2
        angka = input('Masukkan angka: ')
        data = angka.split(" ")
        new_data = []
        for i in range(len(data)):
          new_data.append(int(data[i]))
        break
      except ValueError:
        print("> Oops! Data yang dimasukkan tidak valid. Coba lagi...\n")
  return new_data

def print_data(new_data):
  for i in range(len(new_data)):
    if i != len(new_data) - 1:
      print(new_data[i], end=", ")
    else:
      print(new_data[i])

def main():
  print("="*50)
  print('------------- Program Quick Sort -------------')
  print("="*50)
  print("> Masukkan data angka acak yang ingin diurutkan.")
  print("> Tiap angka dipisah menggunakan Space.")
  print("="*50, "\n")
  state_try = True
  while state_try:
    original_data = input_data()
    clear = True
    while clear:
      state_data = []
      for i in range(len(original_data)):
        state_data.append(original_data[i])
      aksi = pilihAksi()
      if aksi == "1":
        print("\nMelakukan Proses... ")
        quickSort(state_data, 0, len(state_data) - 1)
        print('\nHasil pengurutan keatas: ')
        print_data(state_data)
        state_data = original_data
      elif aksi == "2":
        print("\nMelakukan Proses... ")
        rev_quickSort(state_data, 0, len(state_data) - 1)
        print('\nHasil pengurutan kebawah: ')
        print_data(state_data)
        state_data = original_data
      elif aksi == "3":
        print("\nData sebelumnya: ")
        for i in range(len(original_data)):
          if i != len(original_data) - 1:
            print(original_data[i], end=" ")
          else:
            print(original_data[i])
        print("\nPerbarui data")
        original_data = input_data()
        print("\n> Data berhasil diperbarui!")
      elif aksi == "4":
        clear = False
      else:
        print("Pilihan tidak valid")
    try_again = input("\nIngin menjalankan program kembali? (Y/N): ").upper()
    if try_again == "N":  
      state_try = False
      print("\nTerima kasih telah menggunakan program ini!")
    print("\n")

main()
# 8 7 6 1 0 9 2