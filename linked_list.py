class LinkedList:
	"""
	LinkedList
	"""
	class Node:
		"""
		Node
		"""
		def __init__(self, data, next=None):
			self.data = data
			self.next = next

	def __init__(self, data=None):
		if isinstance(data, list):
			for i in data:
				self.push_back(i)
		if data is None:
			self.head = None
			self.tail = None
			self.size = 0
		else:
			raise TypeError


	def __len__(self):
		return self.size

	def __iter__(self):
		current = self.head
		while current:
			yield current.data
			current = current.next

	def __str__(self):
		return str(list(self))
	
	def __repr__(self):
		return str(self)

	def __getitem__(self, index):
		if index >= self.size:
			raise IndexError
		current = self.head
		for i in range(index):
			current = current.next
		return current.data

	def __setitem__(self, index, value):
		if index >= self.size:
			raise IndexError
		current = self.head
		for i in range(index):
			current = current.next
		current.data = value

	def __delitem__(self, index):
		if index >= self.size:
			raise IndexError
		if index == 0:
			self.head = self.head.next
			self.size -= 1
			return
		current = self.head
		for i in range(index - 1):
			current = current.next
		current.next = current.next.next
		self.size -= 1

	def __contains__(self, value):
		return value in list(self)

	def __eq__(self, other):
		return list(self) == list(other)

	def __ne__(self, other):
		return not self == other

	def __add__(self, other):
		if isinstance(other, LinkedList):
			current = self.head
			while current:
				other.append(current.data)
				current = current.next
			return other
		else:
			raise TypeError

	def __iadd__(self, other):
		return self + other

	def push_back(self, data):
		node = self.Node(data)
		if self.head is None:
			self.head = node
			self.tail = node
		else:
			self.tail.next = node
			self.tail = node
		self.size += 1

	def push_front(self, data):
		node = self.Node(data)
		if self.head is None:
			self.head = node
			self.tail = node
		else:
			node.next = self.head
			self.head = node
		self.size += 1

	def pop_back(self):
		if self.head is None:
			raise IndexError
		if self.head == self.tail:
			self.head = None
			self.tail = None
		else:
			current = self.head
			while current.next != self.tail:
				current = current.next
			current.next = None
			self.tail = current
		self.size -= 1

	def pop_front(self):
		if self.head is None:
			raise IndexError
		self.head = self.head.next
		self.size -= 1