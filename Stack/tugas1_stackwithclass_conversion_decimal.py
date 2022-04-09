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

def programController():
  print("""
==================================================
----------------- Selamat Datang -----------------
------ Program untuk mengkonfersi bilangan -------
==================================================
  """)
  print(50*"=")
  input_user = input("Masukkan angka yang akan dikonversi: ")
  if input_user == "":
    print("\nTidak ada data yang dimasukkan!")
    print(50*"=")
    return
  elif input_user.isnumeric() == False:
    print(f"\nData yang dimasukkan ({input_user}) bukanlah angka!")
    return
  print(50*"=")
  convert = Converter(input_user)
  print(f"""
Angka [Desimal] yang dimasukan adalah : {input_user}
Hasil Konversi:
 - Desimal ke Binary      : {convert.desToBin()}
 - Desimal ke Oktal       : {convert.desToOct()}
 - Desimal ke Hexadesimal : {convert.desToHex()}
  """)

def main():
  state = True
  while state:
    programController()
    yesList = ["Y", 'y', "1"]
    noList = ["N", 'n', "0"]
    stateTry = True
    while stateTry:
      feedback = input("Apakah ingin menjalankan program ini lagi? (Y/N): ")
      if feedback in yesList or feedback in noList:
        stateTry = False
        break
      print(50*"=")
      print("Perintah tidak sesuai!")
      print("Silahkan coba kembali!")
      print(50*"=")
    if feedback in yesList:
      state = True
    elif feedback in noList:
      state = False
  print(50*"=")
  print("Terimakasih telah menggunakan program ini >_<")
  print(50*"=")

main()