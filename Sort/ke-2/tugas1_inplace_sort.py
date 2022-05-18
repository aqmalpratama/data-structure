import time

def inplaceSort(array):
  for i in range(1, len(array)):
    key = array[i]
    j = i - 1
    while j >= 0 and key < array[j]: # jika key lebih kecil dari array[j] 
      time.sleep(0.2)
      print(f'Kunci sekarang {key}, Tukar {array[j]} dengan {array[j + 1]} => {array}')
      array[j + 1] = array[j]
      j -= 1
    array[j + 1] = key
  return array

def rev_inplaceSort(array):
  for i in range(1, len(array)):
    key = array[i]
    j = i - 1
    while j >= 0 and key > array[j]:
      time.sleep(0.2)
      print(f'Kunci sekarang {key}, Tukar {array[j]} dengan {array[j + 1]} => {array}')
      array[j + 1] = array[j]
      j -= 1
    array[j + 1] = key
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
    new_data = input_data()
    clear = True
    while clear:
      aksi = pilihAksi()
      if aksi == "1":
        print("\nMelakukan Proses... ")
        inplaceSort(new_data)
        print('\nHasil pengurutan keatas: ')
        print_data(new_data)
      elif aksi == "2":
        print("\nMelakukan Proses... ")
        rev_inplaceSort(new_data)
        print('\nHasil pengurutan kebawah: ')
        print_data(new_data)
      elif aksi == "3":
        print("\nData sebelumnya: ")
        for i in range(len(new_data)):
          if i != len(new_data) - 1:
            print(new_data[i], end=" ")
          else:
            print(new_data[i])
        print("\nPerbarui data")
        new_data = input_data()
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