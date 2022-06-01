import time

def inplaceSort(array):
  print(f'array awal: {array}')
  n = len(array)
  for i in range(n - 1):
    maximum = array[n - i - 1]
    maximum_idx = 0
    for j in range(n - i - 1):
      if array[j] > maximum:
        maximum = array[j]
        maximum_idx = j

    if not array[n - i - 1] > array[maximum_idx]:
      array[n - i - 1], array[maximum_idx] = array[maximum_idx], array[n - i - 1]
      print(f"{array[n - i - 1]} ditukar dengan {array[maximum_idx]} => {array}")
  print()
  return array

def rev_inplaceSort(array):
  print(f'array awal: {array}')
  n = len(array)
  for i in range(n - 1):
    maximum = array[n - i - 1]
    maximum_idx = 0
    for j in range(n - i - 1):
      if array[j] < maximum:
        maximum = array[j]
        maximum_idx = j

    if not array[n - i - 1] < array[maximum_idx]:
      array[n - i - 1], array[maximum_idx] = array[maximum_idx], array[n - i - 1]
      print(f"{array[n - i - 1]} ditukar dengan {array[maximum_idx]} => {array}")
  print()
  return array

def pilihAksi():
  print("\nDaftar Aksi:\n 1. Mengurutkan Keatas\n 2. Mengurutkan Kebawah\n 3. Perbarui Data\n 4. Keluar")
  pilihan = input("Masukkan pilihan Anda (1, 2, 3, atau 4): ")
  return pilihan

def input_data():
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
  print('------------- Program Inplace Sort -------------')
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
        inplaceSort(state_data)
        print('Hasil pengurutan keatas: ')
        print_data(state_data)
        state_data = original_data
      elif aksi == "2":
        print("\nMelakukan Proses... ")
        rev_inplaceSort(state_data)
        print('Hasil pengurutan kebawah: ')
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