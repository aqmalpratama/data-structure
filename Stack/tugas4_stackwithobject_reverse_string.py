class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, data):
        self.items.append(data)
 
    def pop(self):
        return self.items.pop()

    def clear(self):
        return self.items.clear()
    
    def size(self):
        return len(self.items)
    
def reverseStringStack(string):
  length = len(string)
  stack = Stack()
  for i in range(length):
    stack.push(string[i])
  string = ""
  for i in range(length):
    string += stack.pop()
  return string

def programMembalikString():
  print("""
================================================
---------------- Selamat Datang ----------------
--- Program untuk membalik kalimat atau kata ---
================================================
  """)
  print(48*"=")
  input_user = input("Masukkan kata atau kalimat: ")
  if input_user == "":
    print("\nTidak ada data yang dimasukkan!")
    print(48*"=")
    return
  print(48*"=")
  print(f"Kalimat yang dimasukan oleh user : {input_user}")
  print(f"Kalimat yang setelah dibalik     : {reverseStringStack(input_user)}")
  print(48*"=")

def main():
  state = True
  while state:
    programMembalikString()
    yesList = ["Y", 'y', 1]
    noList = ["N", 'n', 0]
    stateTry = True
    while stateTry:
      feedback = input("Apakah ingin menjalankan program ini lagi? (Y/N): ")
      if feedback in yesList or feedback in noList:
        stateTry = False
        break
      print(48*"=")
      print("\nPerintah tidak sesuai!")
      print("Silahkan coba kembali!")
      print(48*"=")
    if feedback in yesList:
      state = True
    elif feedback in noList:
      state = False
  print(48*"=")
  print('Terimakasih telah menggunakan program ini')
  print(48*"=")

main()