def linearSearch(arr, n, target):
  for i in range(n):
    if arr[i] == target:
			return i
  return -1

def main():
	ingin_lanjut = True
	while ingin_lanjut:
		print('------ Program Binary Search ------\n')
		print('* CATATAN *')
		print('Mohon masukkan angka dengan tanda koma sebagai pemisah. Jika dirasa sudah cukup, maka tekan enter untuk melakukan proses pencarian angka.')
		print('Contoh memasukkan angka : 21, 32, 17, 2, 51')
		angka = input('Masukkan beberapa angka acak: ')
		data = angka.split(", ")
		new_data = []
		for i in range(len(data)):
			new_data.append(int(data[i]))

		target = int(input('Masukkan angka yang ingin dicari: '))
		res = linearSearch(new_data, len(new_data), target)
		if res == -1:
			print('Angka tidak ditemukan')
		else:
			print('Angka ditemukan pada indeks ke-', res)

		print('\n--- Pilihan ---')
		print('1. Program akan dijalankan kembali')
		print('2. Program akan diakhiri')
		konfirmasi = True
		while konfirmasi:
			konfirmasi = input("Apakah Anda ingin menjalankan program ini kembali? (ketik 1 atau 2): ")
			if konfirmasi == '1':
				print("Baik, program dijalankan kembali\n")
				konfirmasi = False
			elif konfirmasi == '2':
				print('Program diakhiri. Sekian, terima kasih\n')
				konfirmasi = ingin_lanjut = False
main()