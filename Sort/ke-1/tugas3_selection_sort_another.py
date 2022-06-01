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
  print("\nDaftar Aksi:\n 1. Mengurutkan Keatas\n 2. Mengurutkan Kebawah\n 3. Perbarui Data\n 4. Keluar")
  pilihan = input("Masukkan pilihan Anda (1, 2, 3, atau 4): ")
  return pilihan

def input_data():
  while True:
      try:
        angka = input('Masukkan angka: ')
        data = angka.split(" ")
        new_data = []
        store_1 = []
        store_2 = []
        for i in range(len(data)):
          new_data.append(int(data[i]))
          store_1.append(int(data[i]))
          store_2.append(int(data[i]))
        break
      except ValueError:
        print("> Oops! Data yang dimasukkan tidak valid. Coba lagi...\n")
  return {'data': new_data, 'store_1': store_1, 'store_2': store_2}

def print_data(new_data):
  for i in range(len(new_data)):
    if i != len(new_data) - 1:
      print(new_data[i], end=", ")
    else:
      print(new_data[i])

def main():
  print("="*50)
  print('------------- Program Selection Sort -------------')
  print("="*50)
  print("> Masukkan data angka acak yang ingin diurutkan.")
  print("> Tiap angka dipisah menggunakan Space.")
  print("="*50, "\n")
  state_try = True
  while state_try:
    data = input_data()
    new_data = data['data']
    store_1 = data['store_1']
    store_2 = data['store_2']
    clear = True
    while clear:
      aksi = pilihAksi()
      if aksi == "1":
        print("\nMelakukan Proses... ")
        selectionSort(store_1)
        print('Hasil pengurutan keatas: ')
        print_data(store_1)
      elif aksi == "2":
        print("\nMelakukan Proses... ")
        rev_selectionSort(store_2)
        print('Hasil pengurutan kebawah: ')
        print_data(store_2)
      elif aksi == "3":
        print("\nData sebelumnya: ")
        for i in range(len(new_data)):
          if i != len(new_data) - 1:
            print(new_data[i], end=" ")
          else:
            print(new_data[i])
        print("\nPerbarui data")
        data = input_data()
        new_data = data['data']
        store_1 = data['store_1']
        store_2 = data['store_2']
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