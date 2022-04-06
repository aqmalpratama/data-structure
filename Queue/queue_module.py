class Queue:
  def __init__(self):
    self.items = []
  
  def enqueue(self, data):
    self.items.append(data)

  def dequeue(self):
    return self.items.pop(0)

antrian = Queue()

antrian.enqueue("Akmal")
antrian.enqueue("Rafi")
antrian.enqueue("Diara")

print(antrian.dequeue())
print(antrian.dequeue())
print(antrian.dequeue())