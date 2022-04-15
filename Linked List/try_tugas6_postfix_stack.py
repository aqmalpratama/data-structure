operator = ['+', '-', '*', '/', '(', ')', '^', '%'] # list of operator
priority = {'+':1, '-':1, '*':2, '/':2, '^':3, '%':4} # Dictionary of operator priority

def infixToPostfix(expression): 
  stack = [] # initialize stack
  output = '' 
  for character in expression:
    print(f'Output : {output}')
    print(f'Character : {character}')
    print(f'Stack : {stack}')
    print('')
    if character not in operator:  # jika karakter bukan operator
      output += character
    elif character == '(':  # jika karakter adalah '('
      stack.append('(')
    elif character == ')': # jika karakter adalah ')'
      while stack and stack[-1] != '(': # looping selama stack tidak kosong dan stack terakhir bukan '('
        output += stack.pop()
      stack.pop()
    else: 
      while stack and stack[-1] !='(' and priority[character] <= priority[stack[-1]]: # looping selama stack tidak kosong dan stack terakhir bukan '(' dan priority karakter lebih kecil atau sama dengan priority stack terakhir
        output += stack.pop()
      stack.append(character)
  print('----------- end loop ------------')
  while stack:
    output += stack.pop()
  return output

def evaluate_postfix(expression):
  stack=[] # empty stack for storing numbers
  for i in expression:
    if i not in operator:
      stack.append(i)  #contains numbers
      print(f'{i} is pushed to stack')
    else:
      print(f'Existing stack is {stack}')
      a = stack.pop() # if ch==operator then pop 2 numbers 
      print(f'{a} is popped from stack')
      b = stack.pop()
      print(f'{b} is popped from stack')
      print(f'{b} {i} {a}')
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
      print(f'Hasil : {res}')
      stack.append(res) # final result 
  return(''.join(map(str,stack)))

# expression = input('Enter the postfix expression ')
# print()
# print('postfix expression entered: ',expression)
# print('Evaluation result: ',evaluate_postfix(expression))

expression = input('Enter infix expression ')
print('infix notation: ',expression)
print('postfix notation: ',infixToPostfix(expression))

# ((1+3)*(6-2)+4-2^3+7/2)%4 -> 13+62-*4+23^72/+4%