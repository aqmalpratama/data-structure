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

def insert(table, key, nama, limit):
    if checkKey(table, key, limit)== True:
        for i in range(limit):
            if len(table[getHashing(key+i, limit)]) == 0:
                table[getHashing(key+i, limit)].append(key)
                table[getHashing(key+i, limit)].append(nama)
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
    print('|    Indeks    |     NIM      |     Nama      |')
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
    print('\nPilihan Aksi:')
    print('1. Tambahkan data ke hash table.')
    print('2. Tampilkan data berdasarkan NIM tertentu.')
    print('3. Hapus data berdasarkan NIM tertentu dari hash table.')
    print('4. Tampilkan semua data dalam hash table.')
    print('5. Hentikan program.')
    pilihan = input('Masukkan pilihan (Ketik 1, 2, 3, 4, atau 5. Lalu, tekan enter): ')
    return pilihan

def main():
    print('==============================================')
    print('||            Program Tabel Hash            ||')
    print('||         - Pengalamatan Terbuka -         ||')
    print('==============================================')

    while True:
        ukuran = input('Masukkan batas maksimal penyimpanan: ')
        if ukuran.isnumeric() == True:
            limit = int(ukuran)
            break
        else:
            print('Harap masukkan angka!')
    table = [[] for _ in range(limit)]
    
    pilihan = pilihanAksi()
    while pilihan != '5':
        if pilihan == '1':
            if checkEmpty(table, limit) == True:
                print('')
                key = input('Masukkan NIM\t: ')
                if key.isnumeric() == True:
                    key = int(key)
                    nama = input('Masukkan nama\t: ')
                    if insert(table, key, nama, limit) == True:
                        print(f'* Data NIM {key} atas nama {nama} berhasil ditambahkan ke table hash. *')
                    else:
                        print(f'* Data NIM {key} atas nama {nama} sudah pernah ditambahkan, gagal menambahkan data. *')
                else:
                    print('* NIM harus berupa angka! *')
            else:
                print("Tabel hash sudah penuh, harap hapus data jika ingin menambahkan data baru!")
        elif pilihan == '2':
            print('')
            key = input('Masukkan NIM dari data yang ingin cari: ')
            if key.isnumeric() == True:
                key = int(key)
                if find(table, key, limit) is not None:
                    nama = find(table, key, limit)
                    print(f'* Data ditemukan *\n* Data dengan NIM {key} adalah : {nama}. *')
                else:
                    print(f'Data dengan NIM {key} tidak ditemukan.')
            else:
                print('NIM harus berupa angka.')
        elif pilihan == '3':
            print('')
            key = input('Masukkan NIM dari data yang ingin Anda hapus: ')
            if key.isnumeric() == True:
                key = int(key)
                nama = find(table, key, limit)
                if delete(table,key,limit)is not None:
                    print(f'* Data atas nama {nama} yang memiliki NIM {key} telah dihapus. *')
                    table[delete(table, key, limit)] = []
                else:
                    print('* Data tidak ditemukan *\n* Data tidak dapat dihapus. *')
            else:
                print('NIM harus berupa angka.')
        elif pilihan == '4':
            print('')
            print('Isi tabel hash: ')
            printHash(table, limit)
        else:
            print('')
            print('Pilihan yang anda masukkan tidak valid.')
            print('')
        pilihan = pilihanAksi()
    print('Terima kasih telah menggunakan program ini.')
main()