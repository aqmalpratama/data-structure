class LinkedList:
  def __init__(self):
    self.items = {}

  def isEmpty(self):
    if self.items == {}:
      return True

  def store(self, next_id, key, value):
    self.items[next_id] = {}
    self.items[next_id]['key'] = key
    self.items[next_id]['value'] = value



llist = LinkedList()
llist.store(1, "mhs", "Akmal")
llist.store(2, "mhs", "Rafi")

print(llist.items)