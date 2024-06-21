#username - complete info
#id1      - 206899163
#name1    - noga arian
#id2      - 318134186
#name2    - Coby Sonnenberg


"""A class represnting a node in an AVL tree"""

class AVLNode(object):
	"""Constructor, you are allowed to add more fields.

	@type key: int or None
	@param key: key of your node
	@type value: string
	@param value: data of your node
	"""
	def __init__(self, key, value):
		self.key = key
		self.value = value
		self.left = None
		self.right = None
		self.parent = None
		self.height = -1
		self.size = 0



	"""returns whether self is not a virtual node 

	@rtype: bool
	@returns: False if self is a virtual node, True otherwise.
	"""
	def is_real_node(self):

		if self.left == None and self.right == None:
			return False
		return True

	"""returns the balance factor of a node
	 @rtype: int
	 @returns: Balance factor of a node
	 """
	def calculate_balance_factor(self):
		left_height = self.left.height
		right_hight = self.right.height
		return left_height - right_hight

	"""returns the height of a node, to be used to check if height of the node
	has changed (out of scope for this function, to be checked outside.
	@rtype: int
	@returns: Height of a node
	"""
	def update_height(self):
		return max(self.right.height, self.left.height) + 1

"""
A class implementing an AVL tree.
"""

class AVLTree(object):

	"""
	Constructor, you are allowed to add more fields.
	@type root: AVLNode Object or None
	@param root: Node to be root of AVLTree
	"""
	def __init__(self):
		self.root = AVLNode(None, None)

	"""searches for a node in the dictionary corresponding to the key

	@type key: int
	@param key: a key to be searched
	@rtype: AVLNode
	@returns: node corresponding to key
	"""
	def search(self, key):
		return None

	"""inserts a new node into the dictionary with corresponding key and value

	@type key: int
	@pre: key currently does not appear in the dictionary
	@param key: key of item that is to be inserted to self
	@type val: string
	@param val: the value of the item
	@rtype: int
	@returns: the number of rebalancing operation due to AVL rebalancing
	"""
	def insert(self, key, val):
		return -1

	"""deletes node from the dictionary

	@type node: AVLNode
	@pre: node is a real pointer to a node in self
	@rtype: int
	@returns: the number of rebalancing operation due to AVL rebalancing
	"""
	def delete(self, node):
		return -1

	"""returns an array representing dictionary 
	An envelope function using the function avl_to_array_rec
	@rtype: list
	@returns: a sorted list according to key of touples (key, value) representing the data structure
	"""
	def avl_to_array(self):
		return self.avl_to_array_rec(self.get_root())

	"""recursive function to return an array representing the dictionary,
	traversing the tree in-order	
	@type node: AVLNode
	@pre: node is a real pointer to a node in self
	@rtype: list
	@returns: a sorted list according to key of touples (key, value)
	"""
	def avl_to_array_rec(self, node):
		if node is None:  # might need update - check if not real node instead
			return []
		return self.avl_to_array_rec(node.left) + [node.key, node.value] + self.avl_to_array_rec(node.right) # check if required tuple

	"""returns the number of items in dictionary 

	@rtype: int
	@returns: the number of items in dictionary 
	"""
	def size(self):
		return -1

	"""compute the rank of node in the dictionary

	@type node: AVLNode
	@pre: node is in self
	@param node: a node in the dictionary to compute the rank for
	@rtype: int
	@returns: the rank of node in self
	"""
	def rank(self, node):
		return -1

	"""finds the i'th smallest item (according to keys) in the dictionary

	@type i: int
	@pre: 1 <= i <= self.size()
	@param i: the rank to be selected in self
	@rtype: AVLNode
	@returns: the node of rank i in self
	"""
	def select(self, i):
		return None

	"""finds the node with the largest value in a specified range of keys

	@type a: int
	@param a: the lower end of the range
	@type b: int
	@param b: the upper end of the range
	@pre: a<b
	@rtype: AVLNode
	@returns: the node with maximal (lexicographically) value having a<=key<=b, or None if no such keys exist
	"""
	def max_range(self, a, b):
		return None

	"""returns the root of the tree representing the dictionary

	@rtype: AVLNode
	@returns: real pointer to the root, None if the dictionary is empty
	"""
	def get_root(self):
		if self.root is not None:
			return self.root
		return None

	"""Function receives a node in the tree where BF has changed to 2 (AVL Criminal) and rotated RR
	@type node: AVLNode
	@param node: AVLNode where BF=2
	"""
	def right_rotation(self, node):
		parent = node.parent
		B = node  # B is original node with BF 2 (root of subtree to rotate)
		A = node.left  # Will be new root of rotated subtree
		B.left = A.right
		B.left.parent = B
		A.parent = parent
		if parent is not None:
			if parent.left == B:
				parent.left = A
			else:
				parent.right = A
		else:
			self.root = A
		A.right = B
		B.parent = A
		return None

	"""Function receives a node in the tree where BF has changed to 2 (AVL Criminal) and rotates LL
	@type node: AVLNode
	@param node: AVLNode where BF=2
	"""
	def left_rotation(self, node):
		parent = node.parent
		B = node  # B is original node with BF 2 (root of subtree to rotate)
		A = node.right  # Will be new root of rotated subtree
		B.right = A.left
		B.right.parent = B
		A.parent = parent
		if parent is not None:
			if parent.left == B:
				parent.left = A
			else:
				parent.right = A
		else:
			self.root = A
		A.left = B
		B.parent = A
		return None

	"""Function receives a node in the tree where BF has changed to 2 (AVL Criminal) and rotates LR
	@type node: AVLNode
	@param node: AVLNode where BF=2
	"""
	def left_then_right_rotation(self, node):
		B = node
		parent = B.parent
		A = B.left
		C = B.left.right
		CL = C.left
		CR = C.right

		if parent is None:
			self.root = C
		else:
			if parent.left == B:
				parent.left = C
			else:
				parent.right = C

		C.parent = parent

		C.left = A
		A.parent = C
		C.right = B
		B.parent = C

		A.right = CL
		CL.parent = A
		B.left = CR
		CR.parent = B
		return None

	"""Function receives a node in the tree where BF has changed to 2 (AVL Criminal) and rotates RL
	@type node: AVLNode
	@param node: AVLNode where BF=2
	"""
	def right_then_left_rotation(self, node):
		B = node
		parent = B.parent
		A = B.right
		C = B.right.left
		CL = C.right
		CR = C.left

		if parent is None:
			self.root = C
		else:
			if parent.left == B:
				parent.left = C
			else:
				parent.right = C

		C.parent = parent

		C.right = A
		A.parent = C
		C.left = B
		B.parent = C

		A.left = CL
		CL.parent = A
		B.right = CR
		CR.parent = B
		return None


## printing trees (call printree(AVLTree))
def printree(t, bykey=True):
	"""Print a textual representation of t
	bykey=True: show keys instead of values"""
	for row in trepr(t, bykey):
		print(row)


# return trepr(t, bykey)

def trepr(t, bykey=False):
	"""Return a list of textual representations of the levels in t
	bykey=True: show keys instead of values"""
	if t == None:
		return ["#"]

	thistr = str(t.key) if bykey else str(t.val)

	return conc(trepr(t.left, bykey), thistr, trepr(t.right, bykey))


def conc(left, root, right):
	"""Return a concatenation of textual represantations of
	a root node, its left node, and its right node
	root is a string, and left and right are lists of strings"""

	lwid = len(left[-1])
	rwid = len(right[-1])
	rootwid = len(root)

	result = [(lwid + 1) * " " + root + (rwid + 1) * " "]

	ls = leftspace(left[0])
	rs = rightspace(right[0])
	result.append(ls * " " + (lwid - ls) * "_" + "/" + rootwid * " " + "\\" + rs * "_" + (rwid - rs) * " ")

	for i in range(max(len(left), len(right))):
		row = ""
		if i < len(left):
			row += left[i]
		else:
			row += lwid * " "

		row += (rootwid + 2) * " "

		if i < len(right):
			row += right[i]
		else:
			row += rwid * " "

		result.append(row)

	return result


def leftspace(row):
	"""helper for conc"""
	# row is the first row of a left node
	# returns the index of where the second whitespace starts
	i = len(row) - 1
	while row[i] == " ":
		i -= 1
	return i + 1


def rightspace(row):
	"""helper for conc"""
	# row is the first row of a right node
	# returns the index of where the first whitespace ends
	i = 0
	while row[i] == " ":
		i += 1
	return i


#########


lst = [i for i in range(5, 15)]
root = AVLNode(20, None)
A = AVLTree()
A.root = root
for i in range(len(lst)):
	if i % 2 == 0:
		root.left = AVLNode(lst[i], None)
		root = root.left
	else:
		root.right = AVLNode(lst[i], None)
#printree(A)


"""
B = AVLTree()
B.insertORIG(8, None)
#printree(B.root)
B.insertORIG(7, None)
#printree(B.root)
B.insertORIG(6, None)
printree(B.get_root())
print(B.root.left.height)

B.right_rotation(B.root.left.left)
printree(B.root)
"""
"""
C = AVLTree()
C.root = AVLNode(3,None)
C.root.left = AVLNode(2,None)
C.root.right = AVLNode(None,None)
C.root.left.parent = C.root
C.root.right.parent = C.root
leftnode = C.root.left
leftnode.left = AVLNode(1,None)
leftnode.right = AVLNode(None,None)
leftnode.left.parent = leftnode
leftnode.right.parent = leftnode
leftleftnode = leftnode.left
leftleftnode.left = AVLNode(0,None)
leftleftnode.right = AVLNode(None,None)
lefty = leftleftnode.left
lefty.left = AVLNode(None,None)
lefty.right = AVLNode(None,None)
lefty.left.parent = lefty
lefty.right.parent = lefty
printree(C.get_root())
"""
"""
C = AVLTree()
C.root = AVLNode(3, None)
C.root.right = AVLNode(4, None)
C.root.left = AVLNode(None, None)
C.root.right.parent = C.root
C.root.left.parent = C.root
rightnode = C.root.right
rightnode.right = AVLNode(5, None)
rightnode.left = AVLNode(None, None)
rightnode.right.parent = rightnode
rightnode.left.parent = rightnode
rightrightnode = rightnode.right
rightrightnode.right = AVLNode(6, None)
rightrightnode.left = AVLNode(None, None)
righty = rightrightnode.right
righty.right = AVLNode(None, None)
righty.left = AVLNode(None, None)
righty.right.parent = righty
righty.left.parent = righty
printree(C.get_root())


C.left_rotation(C.root.right)

printree(C.get_root())
"""
"""
C = AVLTree()
C.root = AVLNode(15, None)

# Level 1
C.root.left = AVLNode(10, None)
C.root.right = AVLNode(22, None)
C.root.left.parent = C.root
C.root.right.parent = C.root

# Level 2
leftnode = C.root.left
rightnode = C.root.right

leftnode.left = AVLNode(4, None)
leftnode.right = AVLNode(11, None)
leftnode.left.parent = leftnode
leftnode.right.parent = leftnode

rightnode.left = AVLNode(20, None)
rightnode.right = AVLNode(24, None)
rightnode.left.parent = rightnode
rightnode.right.parent = rightnode

# Level 3
leftleftnode = leftnode.left
leftrightnode = leftnode.right

leftleftnode.left = AVLNode(2, None)
leftleftnode.right = AVLNode(7, None)
leftleftnode.left.parent = leftleftnode
leftleftnode.right.parent = leftleftnode

leftrightnode.right = AVLNode(12, None)
leftrightnode.right.parent = leftrightnode

rightleftnode = rightnode.left

rightleftnode.left = AVLNode(18, None)
rightleftnode.left.parent = rightleftnode

# Level 4
leftleftleftnode = leftleftnode.left
leftleftrightnode = leftleftnode.right

leftleftleftnode.left = AVLNode(1, None)
leftleftleftnode.right = AVLNode(None, None)
leftleftleftnode.left.parent = leftleftleftnode
leftleftleftnode.right.parent = leftleftleftnode

leftleftrightnode.left = AVLNode(6, None)
leftleftrightnode.right = AVLNode(8, None)
leftleftrightnode.left.parent = leftleftrightnode
leftleftrightnode.right.parent = leftleftrightnode

root = C.root

root.right.right.right = AVLNode(None, None)
root.right.right.right.parent = root.right.right
root.right.right.left = AVLNode(None, None)
root.right.right.left.parent = root.right.right

root.right.left.right = AVLNode(None, None)
root.right.left.right.parent = root.right.left
root.right.left.left.left = AVLNode(None, None)
root.right.left.left.right = AVLNode(None, None)
root.right.left.left.left.parent = root.right.left.left
root.right.left.left.right.parent = root.right.left.left

root.left.left.left.left.left = AVLNode(None,None)
root.left.left.left.left.left.parent = root.left.left.left.left

root.left.left.left.left.right = AVLNode(None,None)
root.left.left.left.left.right.parent = root.left.left.left.left

root.left.left.left.right.left = AVLNode(None,None)
root.left.left.left.right.right = AVLNode(None,None)
root.left.left.left.right.left.parent = root.left.left.left.right
root.left.left.left.right.right.parent = root.left.left.left.right

root.left.left.right.left.left = AVLNode(5,None)
root.left.left.right.left.right = AVLNode(None,None)
root.left.left.right.left.left.parent = root.left.left.right.left
root.left.left.right.left.right.parent = root.left.left.right.left

root.left.left.right.left.left.left = AVLNode(None,None)
root.left.left.right.left.left.right = AVLNode(None,None)
root.left.left.right.left.left.left.parent = root.left.left.right.left.left
root.left.left.right.left.left.right.parent = root.left.left.right.left.left

root.left.left.right.right.left = AVLNode(None,None)
root.left.left.right.right.right = AVLNode(None,None)
root.left.left.right.right.left.parent = root.left.left.right.right
root.left.left.right.right.right.parent = root.left.left.right.right
"""
"""
C = AVLTree()
C.root = AVLNode(50, None)

# Level 1
C.root.right = AVLNode(80, None)
C.root.left = AVLNode(20, None)
C.root.right.parent = C.root
C.root.left.parent = C.root

# Level 2
rightnode = C.root.right
leftnode = C.root.left

rightnode.right = AVLNode(100, None)
rightnode.left = AVLNode(70, None)
rightnode.right.parent = rightnode
rightnode.left.parent = rightnode

leftnode.right = AVLNode(30, None)
leftnode.left = AVLNode(10, None)
leftnode.right.parent = leftnode
leftnode.left.parent = leftnode

# Level 3
rightrightnode = rightnode.right
rightleftnode = rightnode.left

rightrightnode.right = AVLNode(110, None)
rightrightnode.left = AVLNode(98, None)
rightrightnode.right.parent = rightrightnode
rightrightnode.left.parent = rightrightnode

rightleftnode.left = AVLNode(68, None)
rightleftnode.left.parent = rightleftnode

leftrightnode = leftnode.right

leftrightnode.right = AVLNode(40, None)
leftrightnode.right.parent = leftrightnode

# Level 4
rightrightrightnode = rightrightnode.right
rightrightleftnode = rightrightnode.left

rightrightrightnode.right = AVLNode(1, None)
rightrightrightnode.left = AVLNode(None, None)
rightrightrightnode.right.parent = rightrightrightnode
rightrightrightnode.left.parent = rightrightrightnode

rightrightleftnode.right = AVLNode(99, None)
rightrightleftnode.left = AVLNode(90, None)
rightrightleftnode.right.parent = rightrightleftnode
rightrightleftnode.left.parent = rightrightleftnode

root = C.root

root.left.left.left = AVLNode(None, None)
root.left.left.left.parent = root.left.left
root.left.left.right = AVLNode(None, None)
root.left.left.right.parent = root.left.left

root.left.right.left = AVLNode(None, None)
root.left.right.left.parent = root.left.right
root.left.right.right.right = AVLNode(None, None)
root.left.right.right.left = AVLNode(None, None)
root.left.right.right.right.parent = root.left.right.right
root.left.right.right.left.parent = root.left.right.right

root.right.right.right.right = AVLNode(None,None)
root.right.right.right.right.parent = root.right.right.right

root.right.right.right.left = AVLNode(None,None)
root.right.right.right.left.parent = root.right.right.right

root.right.right.left.right.right = AVLNode(None,None)
root.right.right.left.right.left = AVLNode(None,None)
root.right.right.left.right.right.parent = root.right.right.left.right
root.right.right.left.right.left.parent = root.right.right.left.right

root.right.right.left.left.right = AVLNode(95,None)
root.right.right.left.left.left = AVLNode(87,None)
root.right.right.left.left.right.parent = root.right.right.left.left
root.right.right.left.left.left.parent = root.right.right.left.left

root.right.right.left.left.right.right = AVLNode(None,None)
root.right.right.left.left.right.left = AVLNode(None,None)
root.right.right.left.left.right.right.parent = root.right.right.left.left.right
root.right.right.left.left.right.left.parent = root.right.right.left.left.right

root.right.right.left.left.left.right = AVLNode(None,None)
root.right.right.left.left.left.left = AVLNode(None,None)
root.right.right.left.left.left.right.parent = root.right.right.left.left.left
root.right.right.left.left.left.left.parent = root.right.right.left.left.left

printree(C.root)

C.right_then_left_rotation(C.root.right)
printree(C.root)

#C.left_then_right_rotation(C.root.left)

#printree(C.get_root())
"""