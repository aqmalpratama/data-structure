def binarySearch(array, target, low, high):
	print()
	print(f'array: {array}')
	while low <= high:
		mid = low + (high - low) // 2
		print(f'low = {low}, high = {high}, target = {target}')
		print(f'mid = array ke-{mid} = {array[mid]}')
		if array[mid] == target:
			return mid
		elif array[mid] > target:
			print(f'{array[mid]} lebih besar dari {target}, maka akan mencari di bagian kanan')
			high = mid - 1
		else:
			print(f'{array[mid]} lebih kecil dari {target}, maka akan mencari di bagian kiri')
			low = mid + 1

def pilihanAksi():
  print("\nDaftar Aksi:\n 1. Memasukkan data\n 2. Menghapus data\n 3. Lihat Data\n 4. Temukan Data\n 5. Perbarui Data\n 6. Keluar")
  pilihan = input("Masukkan pilihan Anda (ketik 1, 2, 3, 4, 5, atau 6. Lalu, tekan Enter): ")
  return pilihan

def main():
	# print('Contoh memasukkan angka : 21 873 2022 77 2 51 131')
	new_data = []
	while True:
		pilihan = pilihanAksi()

		if pilihan == '1':
			angka = input('Masukkan beberapa angka acak: ')
			data = angka.split(" ")
			success_insert = []
			error_insert = []

			for i in range(len(data)):
				if int(data[i]) in new_data:
					error_insert.append(int(data[i]))
				else:
					new_data.append(int(data[i]))
					success_insert.append(int(data[i]))
			
			if len(error_insert) > 0:
				print(f'{error_insert} sudah ada di dalam array.')
			if len(success_insert) > 0:
				print(f'{success_insert} berhasil dimasukkan ke array.')

		elif pilihan == '2':
			if len(new_data) == 0:
				print('Array kosong. Tidak ada data yang dapat dihapus.')
				main()

			angka = input('Masukkan beberapa angka yanng akan dihapus: ')
			data = angka.split(" ")
			success_delete = []
			error_delete = []
			
			for i in range(len(data)):
				if int(data[i]) in new_data:
					success_delete.append(int(data[i]))
					new_data.remove(int(data[i]))
				else:
					error_delete.append(int(data[i]))

			if len(error_delete) > 0:
				print(f'{error_delete} tidak ada di dalam array.')
			if len(success_delete) > 0:
				print(f'{success_delete} berhasil dihapus dari array.')

		elif pilihan == '3':
			if len(new_data) == 0:
				print('Array kosong. Tidak ada data yang dapat dilihat.')
				main()

			print('Data yang ada di dalam array: ')
			for i in range(len(new_data)):
				if i != len(new_data) - 1:
					print(new_data[i], end=", ")
				else:
					print(new_data[i])

		elif pilihan == '4':
			if len(new_data) == 0:
				print('Array kosong. Tidak ada data yang dapat dicari.')
				main()

			new_data.sort()
			target = int(input('Masukkan angka yang ingin dicari: '))
			res = binarySearch(new_data, target, 0, len(new_data) - 1)
			if res == -1:
				print('Angka tidak ditemukan')
			else:
				print('Angka ditemukan pada indeks ke-', res)

		elif pilihan == '5':
			new_data = []
			angka = input('Masukkan beberapa angka acak: ')
			data = angka.split(" ")
			success_insert = []
			error_insert = []

			for i in range(len(data)):
				if int(data[i]) in new_data:
					error_insert.append(int(data[i]))
				else:
					new_data.append(int(data[i]))
					success_insert.append(int(data[i]))
			
			if len(error_insert) > 0:
				print(f'{error_insert} sudah ada di dalam array.')
			if len(success_insert) > 0:
				print(f'{success_insert} berhasil dimasukkan ke array.')
			
		elif pilihan == '6':
			print('Terima kasih telah menggunakan program ini')
			exit()

		else:
			print('Pilihan tidak ditemukan')

print('------ Program Binary Search ------')
print('* Info *')
print('Masukkan angka dengan spasi sebagai pemisah. Lalu tekan enter untuk melanjutkan proses.')
main()