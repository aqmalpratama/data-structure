class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None

  def insertAtEnd(self, data):
    new_node = Node(data)
    if self.head is None:
      self.head = new_node
      return
    last = self.head
    while (last.next):
      last = last.next
    last.next = new_node

  def deleteFirst(self):
    temp = self.head
    data = temp.data
    self.head = temp.next
    temp = None
    return data

  def deleteLast(self):
    temp = self.head
    while (temp.next):
      prev = temp
      temp = temp.next
    data = temp.data
    prev.next = None
    temp = None
    return data

  def getLast(self):
    temp = self.head
    arr = []
    while (temp):
      arr.append(temp.data) 
      temp = temp.next
    i = len(arr)
    return arr[i - 1]
  
  def isEmpty(self):
    temp = self.head
    if temp is None:
      return True
    else:
      return False

  def getCount(self):
    temp = self.head
    count = 0
    while (temp):
      count += 1
      temp = temp.next
    return count

operator = ['+', '-', '*', '/', '(', ')', '^', '%'] # list of operator
priority = {'+':1, '-':1, '*':2, '/':2, '^':3, '%':4} # Dictionary of operator priority

def infixToPostfix(expression): 
  ll = LinkedList()
  output = '' 
  for character in expression:
    if character not in operator:  # jika karakter bukan operator
      output += character
    elif character == '(':  # jika karakter adalah '('
      ll.insertAtEnd('(')
    elif character == ')': # jika karakter adalah ')'
      while ll.isEmpty() == False and ll.getLast() != '(': # looping selama stack tidak kosong dan stack terakhir bukan '('
        if ll.getCount() > 1:
          output += ll.deleteLast()
        else:
          output +=  ll.deleteFirst()
      if ll.getCount() > 1:
        ll.deleteLast()
      else:
        ll.deleteFirst()
    else: 
      while ll.isEmpty() == False and ll.getLast() != '(' and priority[character] <= priority[ll.getLast()]: # looping selama stack tidak kosong dan stack terakhir bukan '(' dan priority karakter lebih kecil atau sama dengan priority stack terakhir
        if ll.getCount() > 1:
          output += ll.deleteLast()
        else:
          output +=  ll.deleteFirst()
      ll.insertAtEnd(character)
  while ll.isEmpty() is False:
    if ll.getCount() > 1:
      output += ll.deleteLast()
    else:
      output +=  ll.deleteFirst()
  return output

def evaluate_postfix(expression):
  ll = LinkedList()
  for i in expression:
    if i not in operator:
      ll.insertAtEnd(i)
    else:
      if ll.getCount() >= 3:
        a = ll.deleteLast() 
        b = ll.deleteLast()
      elif ll.getCount() == 2:
        a = ll.deleteLast() 
        b = ll.deleteFirst()
      if i == '+':
        res = int(b) + int(a) # old val <operator> recent value
      elif i == '-':
        res = int(b) - int(a)    
      elif i == '*':
        res = int(b) * int(a)
      elif i == '%':
        res = int(b) % int(a) 
      elif i == '/':
        res = int(b) / int(a)
      elif i == '^':
        res = int(b) ** int(a)
      ll.insertAtEnd(res)
  return res

def main():
  print("""
========================================================================
-------------------------- Selamat Datang ------------------------------
------------------- Program Postfix (LinkedList) -----------------------
========================================================================""")
  while True:
    stringInfix = input("Masukkan ekspresi infix : ")
    if stringInfix:
      print(f"Ekspresi infix \t\t: {stringInfix}")
      print(f"Ekspresi postfix \t: {infixToPostfix(stringInfix)}")
      print(f"Hasil nilai ekspresi \t: {evaluate_postfix(infixToPostfix(stringInfix))}")
      break
    else:
      print("Ekspresi tidak boleh kosong")
  
  while True:
    print('\n--- Pilihan ---')
    print('1. Program akan dijalankan kembali')
    print('2. Program akan diakhiri')
    konfirmasi = input("Apakah Anda ingin menjalankan program ini kembali? (ketik 1 atau 2): ")
    if konfirmasi == '1':
      print("Baik, program dijalankan kembali.\n")
      main()
    elif konfirmasi == '2':
      print('Program diakhiri. Sekian, terima kasih.\n')
      break
    else:
      print('* Peringatan *')
      print('Mohon ketik dengan pilihan yang tersedia.')
main()