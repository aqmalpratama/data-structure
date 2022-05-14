def createStack():
  stack = []
  return stack

def size(stack):
  return len(stack)

def isEmpty(stack):
  if size(stack) == 0:
    return True

def push(stack, item):
  stack.append(item)

def pop(stack):
  return stack.pop()
  
def decimalToBinary(angka):
  stack = createStack()
  resConversion = ''
  while angka > 0:
    push(stack, angka % 2)
    angka //= 2
  while isEmpty(stack) != True:
    resConversion += str(pop(stack))
  return resConversion

def decimalToOctal(angka):
  stack = createStack()
  resConversion = ''
  storeBilDec = angka
  while angka > 0:
    push(stack, angka % 8)
    angka = angka // 8
  while isEmpty(stack) != True:
    resConversion += str(pop(stack))
  return resConversion

def decimalToHexadecimal(angka):
  stack = createStack()
  conversion_table = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A' , 'B', 'C', 'D', 'E', 'F']
  resConversion = ''
  while angka > 0:
    push(stack, angka % 16)
    angka = angka // 16
  while isEmpty(stack) != True:
    resConversion += str(conversion_table[pop(stack)])
  return resConversion

def pilihanAksi():
  print("\nDaftar Aksi:\n1. Konversi ke bilangan biner\n2. Konversi ke bilangan oktal\n3. Konversi ke bilangan hexadesimal\n4. Ganti bilangan desimal\n5. Keluar")
  pilihan = input("Masukkan pilihan Anda: ")
  return pilihan

def main():
  print()
  bilDesimal = input("Masukkan bilangan desimal: ")

  if bool(bilDesimal) == False:
    print('* Peringatan *')
    print('Bilangan desimal tidak boleh kosong')
    main()
    
  if bool(bilDesimal) and bool(bilDesimal.isnumeric()) == False:
    print('* Peringatan *')
    print('Bilangan desimal harus diisi dengan angka')
    main()

  if bilDesimal and bool(bilDesimal.isnumeric()):
    bilDesimal = int(bilDesimal)
    
    ulang = True
    while ulang:
      pilihan = pilihanAksi()
      if pilihan == '1':
        print(f"Bilangan desimal: {bilDesimal}")
        print(f"Hasil konversi ke biner: {decimalToBinary(bilDesimal)}")
      elif pilihan == '2':
        print(f"Bilangan desimal: {bilDesimal}")
        print(f"Hasil konversi ke oktal: {decimalToOctal(bilDesimal)}")
      elif pilihan == '3':
        print(f"Bilangan desimal: {bilDesimal}")
        print(f"Hasil konversi ke hexadesimal: {decimalToHexadecimal(bilDesimal)}")
      elif pilihan == '4':
        main()
      elif pilihan == '5':
        print('Progam diakhiri, terima kasih')
        exit()
      else:
        print('\nPilihan tidak valid')

print()
print("""---   TUGAS 1 NO 1 - KONVERSI BILANGAN DESIMAL DENGAN STACK   ---""")
print("ANGGOTA KELOMPOK 3: ")
print("1. AKMAL RAFI DIARA PUTRA            - 1313621007") 
print("2. MUHAMMAD AQMAL KHAFIDZ PRATAMA    - 1313621005") 
print("3. RAWDO MADINA                      - 1313621028") 
print("4. RADEN RORO ZIVA AZZAHRAH KHALILA  - 1313621034") 
print("5. SALWA TSABITAH                    - 1313621042") 
main()