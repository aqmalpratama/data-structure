# asli ni ez banyak beud caranya

# pake loop
def reverseLoop(string):
  reversenya = ""
  for i in string:
    reversenya = i + reversenya
  return reversenya

# pake recursive
def reverseRecursive(string):
    if len(string) == 0:
        return string
    else:
        return reverseRecursive(string[1:]) + string[0]

# pake string slice langsung
def reverseExtendedSlice(string):
    string = string[::-1]
    return string

# pake function reversed juga bisa, tapi perlu function join
def reverseReversed(string):
    string = "".join(reversed(string))
    return string

inputan = input("Masukkan string: ")
print ("Kalimat yang diinput user : " + inputan)
print ("Kalimat yang telah direverse : " + reverseReversed(inputan))