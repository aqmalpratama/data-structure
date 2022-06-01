def mergeSort(array):
  split = False
  if len(array) > 1:
    mid = len(array) // 2
    left = array[:mid]
    right = array[mid:]

    split = True

    print()
    print(f'Memecah array: {array} menjadi {left} dan {right}')
    mergeSort(left)
    mergeSort(right)

    i = j = k = 0
    while i < len(left) and j < len(right):
      if left[i] < right[j]:
        array[k] = left[i]
        i += 1
      else:
        array[k] = right[j]
        j += 1
      k += 1

    while i < len(left):
      array[k] = left[i]
      i += 1
      k += 1

    while j < len(right):
      array[k] = right[j]
      j += 1
      k += 1
  
  if split == True:
    print(f'Digabung: {array}')

def rev_mergeSort(array):
  split = False
  if len(array) > 1:
    mid = len(array) // 2
    left = array[:mid]
    right = array[mid:]

    rev_mergeSort(left)
    rev_mergeSort(right)

    split = True
    print()
    print(f'Memecah array: {array} menjadi {left} dan {right}')

    i = j = k = 0
    while i < len(left) and j < len(right):
      if left[i] > right[j]:
        array[k] = left[i]
        i += 1
      else:
        array[k] = right[j]
        j += 1
      k += 1

    while i < len(left):
      array[k] = left[i]
      i += 1
      k += 1

    while j < len(right):
      array[k] = right[j]
      j += 1
      k += 1

  if split == True:
    print(f'Digabung: {array}')
    

def pilihAksi():
  print("\nDaftar Aksi:\n 1. Mengurutkan Keatas\n 2. Mengurutkan Kebawah\n 3. Perbarui Data\n 4. Keluar")
  pilihan = input("Masukkan pilihan Anda (1, 2, 3, atau 4): ")
  return pilihan

def input_data():
  # 6 5 3 1 8 7 2 4
  while True:
    try:
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
  print('------------- Program Merge Sort -------------')
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
        mergeSort(state_data)
        print('\nHasil pengurutan keatas: ')
        print_data(state_data)
        state_data = original_data
      elif aksi == "2":
        print("\nMelakukan Proses... ")
        rev_mergeSort(state_data)
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