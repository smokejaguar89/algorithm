class Node(object):

	def __init__(self, val, pointer):
		self.val = val
		self.pointer = pointer

class LinkedList(object):

	def __init__(self, head):
		self.head = head

	def print_items(self):
		if self.head:
			current_node = self.head

			while current_node is not None:
				print current_node.val
				current_node = current_node.pointer

	def print_from_head(self, head):
		if head:
			current_node = head

			while current_node is not None:
				print current_node.val
				current_node = current_node.pointer

	def reverse_list(self):
		if self.head:
			current_node = self.head
			prev = None

			while current_node is not None:
				next = current_node.pointer
				current_node.pointer = prev
				prev = current_node
				current_node = next

		return prev

# c -> b -> a -> None

# a -> None
# b -> a



# a -> b -> c -> None
c = Node('c', None)
b = Node('b', c)
a = Node('a', b)

ll = LinkedList(a)
ll.print_items()
ll.print_from_head(ll.reverse_list())
