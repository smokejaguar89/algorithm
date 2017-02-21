# Example Trie insertion implementation
# Efficient look-up for autocomplete implementations

class Node:
  def __init__(self, val, finished):
    self.val = val
    self.finished = finished

  def has_children(self):
    if len(self.children) == 0:
      return False
    return True

  children = []

class Trie:
  root = Node("root", False)

  def insert_val(self, inputt, node=root):

    common = ""
    node_left = ""
    input_left = ""
    depth = 0
    search_range = 0

    if node.has_children():
      for child in node.children:
        if inputt[0] == child.val[0]:
          search_range = len(inputt) if len(inputt) < len(child.val) else len(child.val)

          for i in range(1, search_range):
            if inputt[i] == child.val[i]:
              common += inputt[i]
              depth = i
          node_left = child.val[depth + 1:]
          input_left = inputt[depth + 1:]

          if input_left == "" and node_left == "":
            return "Node with value already exists"

          elif input_left == "":
            child.val = common
            new_node = Node(node_left, False)
            if child.has_children():
              new_node.children = child.children
              child.children = []
              child.children.append(new_node)
            return "Added new node: " + node_left

          elif node_left == "":
            if child.has_children():
              return self.insert_val(input_left, child)

      new_node = Node(inputt, False)
      node.children.append(new_node)
      return "Added new node with value: " + inputt

    else:
      new_node = Node(inputt, False)
      node.children.append(new_node)
      return "Added first node with value: " + inputt

my_trie = Trie()
print my_trie.insert_val("water")
print my_trie.insert_val("slow")
print my_trie.insert_val("slower")
print my_trie.insert_val("slo")
