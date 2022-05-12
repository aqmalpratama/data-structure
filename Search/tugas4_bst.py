class BSTNode:
	def __init__(self, val=None):
		self.left = None
		self.right = None
		self.val = val

	def insert(self, val):
		if not self.val:
			self.val = val
			return

		if self.val == val:
			return

		if val < self.val:
			if self.left:
				self.left.insert(val)
				return
			self.left = BSTNode(val)
			return

		if self.right:
			self.right.insert(val)
			return
		self.right = BSTNode(val)

	def get_min(self):
		current = self
		while current.left is not None:
			current = current.left
		return current.val

	def get_max(self):
		current = self
		while current.right is not None:
			current = current.right
		return current.val

	def delete(self, val):
		if self == None:
			return self
		if val < self.val:
			if self.left:
				self.left = self.left.delete(val)
			return self
		if val > self.val:
			if self.right:
				self.right = self.right.delete(val)
			return self
		if self.right == None:
			return self.left
		if self.left == None:
			return self.right
		min_larger_node = self.right
		while min_larger_node.left:
			min_larger_node = min_larger_node.left
		self.val = min_larger_node.val
		self.right = self.right.delete(min_larger_node.val)
		return self

	def exists(self, val):
		if val == self.val:
			return True

		if val < self.val:
			if self.left == None:
				return False
			return self.left.exists(val)

		if self.right == None:
			return False
		return self.right.exists(val)

	def preorder(self, vals):
		if self.val is not None:
			vals.append(self.val)
		if self.left is not None:
			self.left.preorder(vals)
		if self.right is not None:
			self.right.preorder(vals)
		return vals

	def inorder(self, vals):
		if self.left is not None:
			self.left.inorder(vals)
		if self.val is not None:
			vals.append(self.val)
		if self.right is not None:
			self.right.inorder(vals)
		return vals

	def postorder(self, vals):
		if self.left is not None:
			self.left.postorder(vals)
		if self.right is not None:
			self.right.postorder(vals)
		if self.val is not None:
			vals.append(self.val)
		return vals

def pilihAksi():
  print("Daftar Aksi:\n 1. Telusuri Secara Preorder\n 2. Telusuri Secara Postorder\n 3. Telusuri Secara Inorder\n 4. Cari Data\n 5. Hapus Data\n 6. Keluar")
  pilihan = input("Masukkan pilihan Anda (1, 2, atau 3): ")
  return pilihan
	
def main():
	print('------ Program BST------')
	print('* CATATAN *')
	print('Mohon masukkan angka dengan tanda koma sebagai pemisah.\nJika dirasa sudah cukup, maka tekan enter untuk melakukan proses pengurutan angka.')
	print('Contoh memasukkan angka : 12, 6, 18, 19, 21, 11, 3, 5, 4, 24, 18')

	angka = input('Masukkan beberapa angka acak: ')
	data = angka.split(", ")
	nums = []
	for i in range(len(data)):
		nums.append(int(data[i]))
	# nums = [12, 6, 18, 19, 21, 11, 3, 5, 4, 24, 18]
	bst = BSTNode()
	for num in nums:
			bst.insert(num)
	
	run = True
	while run:
		pilihan = pilihAksi()
		if pilihan == '1':
			print("preorder:")
			print(bst.preorder([]))
			print("")
		elif pilihan == '2':
			print("postorder:")
			print(bst.postorder([]))
			print("")
		elif pilihan == '3':
			print("inorder:")
			print(bst.inorder([]))
			print("")
		elif pilihan == '4':
			cari = int(input("Masukkan angka yang ingin dicari: "))
			if bst.exists(cari):
				print("Angka", cari, "ada di dalam BST")
			else:
				print("Angka", cari, "tidak ada di dalam BST")
			print()
		elif pilihan == '5':
			delete_angka = input('Masukkan beberapa angka acak: ')
			data_delete = delete_angka.split(", ")
			nums = []
			for i in range(len(data_delete)):
				nums.append(int(data_delete[i]))
			# nums = [2, 4, 5]
			print("deleting " + str(nums))
			for num in nums:
				bst.delete(num)
			print("")
		else:
			print("Terima Kasih")
			run = False

	# print("4 exists:")
	# print(bst.exists(4))
	# print("2 exists:")
	# print(bst.exists(2))
	# print("12 exists:")
	# print(bst.exists(12))
	# print("18 exists:")
	# print(bst.exists(18))

main()