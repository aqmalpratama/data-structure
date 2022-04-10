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
    if self.head is None:
      return
    temp = self.head
    if temp.kode == kode:
      self.head = temp.next
      temp = None
      return

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