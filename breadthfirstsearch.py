class Node():

  def __init__(self, val, *args):
    self.marked = False
    self.val = val
    self.pointers = args

a = Node(33)
b = Node(99, a)
c = Node(3, b)
d = Node(7)
e = Node(2, d)
f = Node(10)
g = Node(8)
h = Node(6, f, g)
i = Node(1, c, e, h)

def is_connected(root, end):

  # enqueue = insert(0, node)
  # dequeue = pop()

  queue = []
  root.marked = True
  queue.insert(0, root)

  while queue:
    r = queue.pop()

    for node in r.pointers:
      if node.marked == False:
        if node.val == end.val:
          return True
        else:
          node.marked = True
          queue.insert(0, node)

  return False

print is_connected(i, f)
