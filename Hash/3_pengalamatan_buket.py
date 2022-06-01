class node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class hashTable:
    def __init__(self, max):
        self.size = max
        self.array = [None for i in range(self.size)]
    
    def getHash(self, key):
        index = key % self.size
        return index

    def insert(self, key_val, value):
        index = self.getHash(key_val)
        if self.array[index] != None:
            state = 0
            temp = self.array[index]
            if temp.key == key_val:
                state = 1
                return False
            while temp.next != None:
                if temp.key == key_val:
                    state = 1
                    return False
                    break
                temp = temp.next
            if state == 0:
                temp.next = node(key_val,value)
                return True 
        else:
            self.array[index] = node(key_val,value)
            return True
            
    def find(self, key_val):
        index = self.getHash(key_val)
        temp = self.array[index]
        while temp != None:
            if temp.key == key_val:
                return temp.value
            temp = temp.next

    def delete(self, key):
        if self.find(key) is None:
            return False
        else:
            index = self.getHash(key)
            if self.array[index].key == key:
                self.array[index] = self.array[index].next
                return True
            else:
                temp = self.array[index]
                while temp.next.key != key:
                    temp = temp.next
                temp.next = temp.next.next
                return True
            
    def listHash(self):
        for i in range(self.size):
            print(f'Indeks ke-{i}',end = " -> ")
            temp = self.array[i]
            while temp != None:
                print(f'({temp.key} : {temp.value})', end = ", ")
                temp = temp.next
            print('( )')

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
    print('||          - Pengalamatan Buket -          ||')
    print('==============================================')

    while True:
        limit = input('Masukkan batas maksimal penyimpanan: ')
        if limit.isnumeric() == True:
            limit = int(limit)
            break
        else:
            print('Harap masukkan angka!')
    
    ht = hashTable(limit)

    pilihan = pilihanAksi()
    while pilihan != '5':
        if pilihan == '1':
            print('')
            print('Silahkan masukkan data dengan format key berupa kombinasi 3 angka dan nama berupa nama mahasiswa.')
            print('')
            key = input('Masukkan key: ')
            if key.isnumeric() == True and len(key) == 3:
                key = int(key)
                value = input('Masukkan nama: ')
                if ht.insert(key, value) == True:
                    print(f'* Data key {key} atas nama {value} berhasil ditambahkan ke table hash. *')
                else:
                    print(f'* Data key {key} atas nama {value} sudah pernah ditambahkan, gagal menambahkan data. *')
            else:
                print('* Key harus berupa angka 3 digit! *')
        elif pilihan == '2':
            print('')
            key = input('Masukkan key dari data yang anda cari: ')
            if key.isnumeric() == True and len(key) == 3:
                key = int(key)
                if ht.find(key) is not None:
                    value = ht.find(key)
                    print(f'* Data ditemukan *\n* Data dengan key {key} adalah {value}. *')
                else:
                    print(f'* Data dengan key {key} tidak ditemukan. *')
            else:
                print('* Key harus berupa angka 3 digit! *')
        elif pilihan == '3':
            print('')
            key = input('Masukkan key dari data yang ingin Anda hapus: ')
            if key.isnumeric() == True and len(key) == 3:
                key = int(key)
                value = ht.find(key)
                if ht.delete(key)==True:
                    ht.delete(key)
                    print(f'* Data atas nama {value} yang memiliki key {key} telah dihapus. *')
                else:
                    print('* Data tidak ditemukan *\n* Data tidak dapat dihapus. *')
            else:
                print('Key harus berupa angka 3 digit!')
        elif pilihan == '4':
            print('')
            print('isi hash table: ')
            ht.listHash()
        else:
            print('')
            print('Pilihan yang Anda masukkan tidak valid.')
        pilihan = pilihanAksi()
    print('Terima kasih telah menggunakan program ini.')

main()
    