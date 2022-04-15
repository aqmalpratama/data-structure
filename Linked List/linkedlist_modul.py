# Create a node
class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None

  # Insert at the beginning
  def insertAtBeginning(self, data):
    new_node = Node(data)
    new_node.next = self.head
    self.head = new_node

  def insertAtAfter(self, key, data):
    new_node = Node(data)
    current = self.head
    while current is not None:
      if current.data == key:
        new_node.next = current.next
        current.next = new_node
        return
      current = current.next
    return False

  # Insert at the end
  def insertAtEnd(self, data):
    new_node = Node(data)
    if self.head is None:
        self.head = new_node
        return
    last = self.head
    while (last.next):
      last = last.next
    last.next = new_node

  # Deleting
  def deleteData(self, data):
    current = self.head
    if current is not None:
      if current.data == data:
        self.head = current.next
        current = None
        return
    while current is not None:
      if current.data == data:
        break
      prev = current
      current = current.next
    if current is None:
      return
    prev.next = current.next
    current = None

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

  # Search an element
  def searchData(self, key):
    current = self.head
    while current is not None:
      if current.data == key:
        return current
      current = current.next
    return False

  def printFromFirst(self):
    temp = self.head
    count = 1
    while (temp):
      print(f"No.{count} {temp.data}")
      count+=1
      temp = temp.next

  def printFromLast(self):
    temp = self.head
    arr = []
    while (temp):
      arr.append(temp.data) 
      temp = temp.next
    count = 1
    i = len(arr)
    while (i != 0):
      print(f"No.{count} {arr[i-1]}")
      count+=1
      i-=1

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

ll = LinkedList()
ll.insertAtEnd('')