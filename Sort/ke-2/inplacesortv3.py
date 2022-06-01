# DONE

# In-Place Sort

data = []

intro = f'''
-------------------------------
Perhitungan Program In-Place Sort
-------------------------------
Dalam perhitungan ini, terdapat beberapa pilihan yang dapat dilakukan pada program ini.
~ (1) -> Masukkan angka.
~ (2) -> Keluar dari program.

Masukkan pilihan yang ingin anda eksekusi = '''

def garis(angka):
    print(angka * '=')

def utama ():
    print()
    garis(28)
    print('Program Membuat In-Place Sort')
    garis(28)
    print(end='')

    count = '\'Melakukan Perhitungan\''
    check = '\'Menampilkan Perhitungan\''

    input_user1 = input(intro)

    if input_user1 == '1':
        print()
        print(f'Anda memilih pilihan {count}.')
        input_user = list(map(int, input(f'Masukkan angka yang akan di eksekusi = ').split()))
        program_count(input_user)
    elif input_user1 == '2':
        print("Terima kasih telah menggunakan program kami!")
        exit()
    else:
        print()
        print('Anda salah memasukkan kata kunci. Periksa kembali kata kunci yang anda masukkan.')
        utama()

    ulang()

def program_count(input_user):
    old = input_user.copy()
    print('Data yang anda masukkan adalah ', end='')
    print(' '.join(map(str, old)))
    pilih = int(input("Silahkan pilih sorting secara ascending(1) atau descending(2): "))
    pjg = len(old)
    if pilih == 1:
        print("Proses dari pengurutan In-Place Sort secara ascending yaitu: ")
        for i in range(pjg - 1):
            max = old[pjg - i - 1]
            maxidx = 0
            for j in range(pjg - i - 1):
                if old[j] > max:
                    max = old[j]
                    maxidx = j

            if not old[pjg - i - 1] > old[maxidx]:
                old[pjg - i - 1], old[maxidx] = old[maxidx], old[pjg - i - 1]
                print(f"{old[pjg - i - 1]} ditukar dengan {old[maxidx]} \t=> ", end='')
                print(' '.join(map(str, old)))
        print("\nHasil dari sortingan menggunakan algoritma In-Place Sort:")
        print(' '.join(map(str, old)))
        print()

    elif pilih == 2:
        print("Proses dari pengurutan In-Place Sort secara descending yaitu: ")
        for i in range(pjg - 1):
            max = old[pjg - i - 1]
            maxidx = 0
            for j in range(pjg - i - 1):
                if old[j] < max:
                    max = old[j]
                    maxidx = j

            if not old[pjg - i - 1] < old[maxidx]:
                old[pjg - i - 1], old[maxidx] = old[maxidx], old[pjg - i - 1]
                print(f"{old[pjg - i - 1]} ditukar dengan {old[maxidx]} \t=> ", end='')
                print(' '.join(map(str, old)))
        print("\nHasil dari sortingan menggunakan algoritma In-Place Sort:")
        print(' '.join(map(str, old)))
        print()



    menu = input("Apakah ingin mengulang pemilihan urutan In-Place Sort? [y/n] ")
    if menu == 'y':
        program_count(input_user)
    else:
        print("Terimakasih!")

def ulang():
    print()
    print(24 * '=' + ' Program telah berakhir ' + '=' * 24)
    input_lanjutan = input(("""
Apakah anda masih ingin mencobanya kembali?
1. Ketik 'Y' atau 'y' jika ingin melanjutkan pemrograman kembali.
2. Ketik 'N' atau 'n' jika ingin keluar dari program.

Masukkan kata kunci yang ingin anda proses : """)).upper()

    if input_lanjutan == 'Y':
        utama()
    elif input_lanjutan == 'N':
        print('\nTerima kasih telah menjalankan Program In-Place Sort\n')
        exit()
    else :
        print('\nAnda salah memasukkan kata kunci. Periksa kembali kata kunci yang anda masukkan.')
        ulang()

utama()