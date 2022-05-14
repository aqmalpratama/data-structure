import time

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
  if isEmpty(stack):
    return "stack is empty"
  return stack.pop()

def reverseStringStack(string):
  length = len(string)
  stack = createStack()
  for i in range(length):
    push(stack, string[i])
  string = ""
  print("Proses membalik kata atau kalimat")
  for i in range(length):
    string += pop(stack)
    time.sleep(0.2)
    print(string)
  return string

def main():
  cobaLagi = True
  while cobaLagi:
    print("--- Program Membalik Kata atau Kalimat ---")
    kata_tidak_kosong = True
    while kata_tidak_kosong:
      inputString = input("Masukkan kata atau kalimat: ")
      if inputString:
        kata_tidak_kosong = False
      else:
        print('Kata atau kalimat tidak boleh kosong.')
    print(f"Kalimat yang telah dibalik : {reverseStringStack(inputString)}")
    reconfirm = True
    while reconfirm:
      print('\n--- Pilihan ---')
      print('1. Program akan dijalankan kembali')
      print('2. Program akan diakhiri')
      konfirmasi = input("Apakah Anda ingin menjalankan program ini kembali? (ketik 1 atau 2 lalu tekan Enter): ")
      if konfirmasi == '1':
        print("Baik, program dijalankan kembali\n")
        reconfirm = False
      elif konfirmasi == '2':
        print('Program diakhiri. terima kasih\n')
        reconfirm = cobaLagi = False
      else:
        print('* Peringatan *')
        print(f'Pilihan tidak valid')
main()