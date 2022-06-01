def getHashing(x,limit):
    return x % limit

def checkKey(table, key, limit):
    for i in range(limit):
        if len(table[i]) > 0:
            if table[i][0] == key:
                return False
    return True

def checkEmpty(table, limit):
    for i in range(limit):
        if len(table[i]) == 0:
            return True
    return False

def insert(table, key, value, limit):
    if checkKey(table, key, limit)== True:
        for i in range(limit):
            if len(table[getHashing(key+i, limit)]) == 0:
                table[getHashing(key+i, limit)].append(key)
                table[getHashing(key+i, limit)].append(value)
                return True

def find(table, key, limit):
    for i in range(limit):
        if len(table[i]) > 0:
            if table[i][0] == key:
                return table[i][1]

def delete(table, key, limit):
    for i in range(limit):
        if len(table[i]) > 0:
            if table[i][0] == key:
                return i

def lines(n):
    print(n* ' ', end='')

def printHash(table, limit):
    print('|=============================================|')
    print('|                  Tabel Hash                 |')
    print('|=============================================|')
    print('|    Indeks    |      NIM     |      Nama     |')
    print('|=============================================|')
    for i in range(limit):
        if len(table[i]) > 0:
            index_space = len(str(i))
            nim_space = len(str(table[i][0]))
            nama_space= len(str(table[i][1]))
            print(f'|{i}',end ='')
            lines(14 - index_space)
            print(f'|{table[i][0]}',end='')
            lines(14 - nim_space)
            print(f'|{table[i][1]}',end='')
            lines(15 - nama_space)
            print(f'|')
        else:
            print(f'|              |              |               |')
    print('|=============================================|')

def pilihanAksi():
    print('Pilihan Aksi:')
    print('1. Tambahkan data ke hash table.')
    print('2. Tampilkan data berdasarkan NIM tertentu.')
    print('3. Hapus data berdasarkan NIM tertentu dari hash table.')
    print('4. Tampilkan semua data dalam hash table.')
    print('5. Hentikan program.')
    pilihan = input('Masukkan pilihan (1, 2, 3, 4, atau 5. Lalu, tekan enter): ')
    return pilihan

def main():
    print('===== Selamat Datang di Program Hash Table =====')
    print('')
 
    while True:
        ukuran = input('Masukkan ukuran array untuk penyimpanan: ')
        if ukuran.isnumeric() == True:
            limit = int(ukuran)
            break
        else:
            print('Tolong masukkan angka!')
    table = [[] for _ in range(limit)]
    
    pilihan = pilihanAksi()
    while pilihan != '5':
        if pilihan == '1':
            if checkEmpty(table, limit)== True:
                print('')
                key = input('Masukkan NIM\t: ')
                if key.isnumeric() == True:
                    key = int(key)
                    value = input('Masukkan nama\t: ')
                    if insert(table, key, value, limit) == True:
                        print(f'Data NIM {key} atas nama {value} berhasil ditambahkan ke table hash.')
                    else:
                        print(f'Data NIM {key} atas nama {value} sudah pernah ditambahkan, gagal dimasukkan ke table hash.')
                else:
                    print('NIM yang anda masukkan tidak valid.')
            else:
                print("Tabel hash sudah penuh, harap hapus data jika ingin menambahkan data baru!")
            print('')
        elif pilihan == '2':
            print('')
            key = input('Masukkan NIM dari data yang ingin cari: ')
            if key.isnumeric() == True:
                key = int(key)
                if find(table, key, limit) is not None:
                    value = find(table, key, limit)
                    print(f'Data dengan NIM {key} adalah : {value}')
                else:
                    print(f'Data dengan NIM {key} tidak ditemukan.')
            else:
                print('NIM yang Anda masukkan tidak valid.')
            print('')
        elif pilihan == '3':
            print('')
            key = input('Masukkan NIM dari data yang ingin Anda hapus: ')
            if key.isnumeric() == True:
                key = int(key)
                value = find(table, key, limit)
                if delete(table,key,limit)is not None:
                    print(f'Data dengan nama {value} yang memiliki NIM {key} telah dihapus.')
                    table[delete(table, key, limit)] = []
                else:
                    print('data tidak ditemukan, sehingga tidak dapat dihapus.')
            else:
                print('NIM yang anda masukkan tidak valid')
            print('')
        elif pilihan == '4':
            print('')
            print('isi hash table: ')
            printHash(table, limit)
            print('')
        else:
            print('')
            print('Pilihan yang anda masukkan tidak valid.')
            print('')
        pilihan = pilihanAksi()
    print('Terima kasih telah menggunakan program ini.')
main()