class Stack:
  def __init__(self):
    self.items = []

  def is_empty(self):
    if self.items == []:
      return True

  def push(self, data):
    self.items.append(data)
 
  def pop(self):
    return self.items.pop()
    
  def size(self):
    return len(self.items)

class Converter:
  def __init__(self, data):
    self.data = data

  def desToBin(self):
    stack = Stack()
    result = ''
    angka = int(self.data)
    while angka > 0:
      stack.push(angka%2)
      angka //= 2
    while stack.is_empty() != True:
      result += str(stack.pop())
    return result

  def desToOct(self):
    stack = Stack()
    result = ''
    angka = int(self.data)
    while angka > 0:
      stack.push(angka%8)
      angka //= 8
    while stack.is_empty() != True:
      result += str(stack.pop())
    return result

  def desToHex(self):
    stack = Stack()
    result = ''
    angka = int(self.data)
    outList = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A' , 'B', 'C', 'D', 'E', 'F']
    while angka > 0:
      stack.push(angka%16)
      angka //= 16
    while stack.is_empty() != True:
      result += str(outList[stack.pop()])
    result = result[::1]
    return result 

def pilihanAksi():
  print("\nDaftar Aksi Konversi:\n1. Desimal ke biner\n2. Desimal ke oktal\n3. Desimal ke hexadesimal\n4. Ganti bilangan desimal\n5. Keluar")
  pilihan = input("Masukkan pilihan Anda (1, 2, 3, 4, 5, atau 6 dan tekan Enter): ")
  return pilihan

def main():
  print()
  bilDesimal = input("Masukkan bilangan desimal: ")

  if bool(bilDesimal) == False:
    print('\n* Peringatan *')
    print('Bilangan desimal tidak boleh kosong')
    main()
    
  if bool(bilDesimal) and bool(bilDesimal.isnumeric()) == False:
    print('\n* Peringatan *')
    print('Bilangan desimal harus diisi dengan angka')
    main()

  if bilDesimal and bool(bilDesimal.isnumeric()):
    bilDesimal = int(bilDesimal)
    convert = Converter(bilDesimal)
    ulang = True
    while ulang:
      pilihan = pilihanAksi()
      if pilihan == '1':
        print(f"\nBilangan desimal: {bilDesimal}")
        print(f"Hasil konversi ke biner: {convert.desToBin()}")
      elif pilihan == '2':
        print(f"\nBilangan desimal: {bilDesimal}")
        print(f"Hasil konversi ke oktal: {convert.desToOct()}")
      elif pilihan == '3':
        print(f"\nBilangan desimal: {bilDesimal}")
        print(f"Hasil konversi ke hexadesimal: {convert.desToHex()}")
      elif pilihan == '4':
        main()
      elif pilihan == '5':
        print('Progam diakhiri, terima kasih >_<')
        exit()
      else:
        print('\nPilihan tidak valid')

print()
print("""---   TUGAS 1 NO 1 - KONVERSI BILANGAN DESIMAL DENGAN STACK MENGGUNAKAN METODE OBJEK   ---""")
print("ANGGOTA KELOMPOK 3: ")
print("1. AKMAL RAFI DIARA PUTRA            - 1313621007") 
print("2. MUHAMMAD AQMAL KHAFIDZ PRATAMA    - 1313621005") 
print("3. RAWDO MADINA                      - 1313621028") 
print("4. RADEN RORO ZIVA AZZAHRAH KHALILA  - 1313621034") 
print("5. SALWA TSABITAH                    - 1313621042") 
main()