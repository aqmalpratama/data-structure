# Create a node
class Node:
  def __init__(self, kode, nama):
    self.kode = kode
    self.nama = nama
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None

  # Insert at the beginning
  def insertAtBeginning(self, kode, nama):
    new_node = Node(kode, nama)
    new_node.next = self.head
    self.head = new_node

  # Insert after a node
  def insertAfter(self, prev_node, new_data):
    if prev_node is None:
      print("The given previous node must inLinkedList.")
      return
    new_node = Node(new_data)
    new_node.next = prev_node.next
    prev_node.next = new_node

  # Insert at the end
  def insertAtEnd(self, kode, nama):
    new_node = Node(kode, nama)
    if self.head is None:
        self.head = new_node
        return
    last = self.head
    while (last.next):
      last = last.next
    last.next = new_node

  # Deleting
  def deleteByCode(self, kode):
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

  # Search an element
  def searchByCode(self, key):
    current = self.head
    while current is not None:
      if current.kode == key:
        return current
      current = current.next
    return False

  # Print the linked list
  def printList(self):
    temp = self.head
    while (temp):
      print(f'{temp.kode} : {temp.nama}')
      temp = temp.next

  # Sort the linked list
  def sortLinkedList(self, head):
    current = head
    index = Node(None)

    if head is None:
      return
    else:
      while current is not None:
        # index points to the node next to current
        index = current.next

        while index is not None:
          if current.data > index.data:
              current.data, index.data = index.data, current.data

          index = index.next
        current = current.next

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

  def sortDataToArray(self):
    size = self.getCount()
    arr = []
    temp = self.head
    while (temp):
      arr.append(temp.data)
      temp = temp.next
    arr.sort()
    i = 0
    while (i < size):
      print(f'{arr[i]}')
      i += 1