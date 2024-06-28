#username - complete info
#id1      - 206899163
#name1    - noga arian
#id2      - 318134186
#name2    - Coby Sonnenberg


"""A class representing a node in an AVL tree"""

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
		if self.key is None and self.value is None:
			return False
		return True

	"""returns the balance factor of a node
	 @rtype: int
	 @returns: Balance factor of a node
	 """
	def calculate_balance_factor(self):
		left_height = self.left.height
		right_height = self.right.height
		return left_height - right_height

	""" Calculates and returns the height of a node
	@rtype: int
	@returns: height of a node
	@post: node's height field not updated within this method
	"""
	def check_height(self):
		return max(self.right.height, self.left.height) + 1

	""" Calculates and returns the size of the subtree of a node
	@rtype: int
	@returns: size of the subtree of the node, including the node
	@post: node's size field not updated within this method
	"""
	def check_size(self):
		return self.left.size + self.right.size + 1

	""" Method that finds the successor of given node in tree
	@param node: AVLNode to find successor of	
	@return: Successor of given node
	@rtype: AVLNode
	"""
	def successor(self):
		if self.right is not None:
			return self.find_min_in_subtree(self.right)
		node_y = self.parent
		node_x = self
		while node_y is not None and node_x is node_y.right:
			node_x = node_y
			node_y = node_x.parent
		return node_y

	""" Method that finds the minimum value in the subtree of the node
	@param node: AVLNode to be searched
	@return: AVLNode with minimum value in the subtree of the node
	@rtype: AVLNode
	"""
	@staticmethod
	def find_min_in_subtree(node):
		while node.left is not None:
			node = node.left
		return node

	""" Function that creates and adds two virtual sons for given node
	@param self: leaf node with no sons 
	@return: None
	"""
	def add_virtual_sons(self):
		self.left = AVLNode(None, None)
		self.left.parent = self
		self.right = AVLNode(None, None)
		self.right.parent = self


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
	@post: inserted a new node but did not update parent heights 
	"""
	def insert(self, key, val):

		node_y, node_x = None, self.root

		while node_x.is_real_node():
			node_y = node_x
			if key < node_x.key:
				node_x = node_x.left
			else:
				node_x = node_x.right

		#  Arrived at a virtual node
		if node_y is None:  # tree is empty
			self.root.key = key
			self.root.value = val
			self.root.height = 0
			self.root.size = 1
			self.root.add_virtual_sons()

		else:
			node_x.key = key
			node_x.value = val
			node_x.height = 0
			node_x.size = 1
			node_x.add_virtual_sons()
			self._insertion_fix(node_x.parent)
		return

	""" Method that climbs to root and fixes  AVL Tree
	@pre: new node already added to tree, called from insert method only
	@param node_y: parent AVLNode of inserted node
	"""
	def _insertion_fix(self, node_y):

		while node_y is not None:
			original_y_height = node_y.height
			node_y.height = node_y.check_height()
			node_y.size += 1
			bf = node_y.calculate_balance_factor()
			if abs(bf) < 2:
				if original_y_height == node_y.height:
					self._update_up(node_y.parent)  # update sizes and heights up
					return
				else:
					node_y = node_y.parent
			else:  # |bf| = 2
				self.pick_rotation(node_y)
				self._update_up(node_y.parent.parent)
				return
		return

	""" Method that climbs to root and fixes size and height of nodes 
	@pre: validated that no rotations are needed from the param node up
	@param node: AVLNode from which to update size and heights of nodes
	@post: updated nodes' size and height fields
	"""
	def _update_up(self, node):
		while node is not None:
			node.height = node.check_height()
			node.size = node.check_size()
			node = node.parent
		return

	"""deletes node from the dictionary

	@type node: AVLNode
	@pre: node is a real pointer to a node in self
	@rtype: int
	@returns: the number of rebalancing operation due to AVL rebalancing
	"""
	def delete(self, node):
		originalparent = node.parent
		if self.node.left is None and self.node.right is None: #node is a leaf
			self.originalparent.add_virtual_sons() #delete the pointer of the parent to node and creat 2 virtual sons
		elif self.node.left is None ^ self.node.right is None: # node has only one child (I used ^ as xor)
			if self.node.left is None: #there is a right son
				node.right.parent = originalparent
				originalparent.right = node.right #created a bypass
			else: #there is a left son
				node.left.parent = originalparent
				originalparent.left = node.right  # created a bypass
		else: #node has 2 children (therefore its successor has no left child)
			nodesucc = self.successor(node)

			if nodesucc.parent.left is nodesucc:
				nodesuccisleftson = True
			else:
				nodesuccisleftson = False

			nodesucc.parent.right = nodesucc.right #remove successor from the tree
			nodesucc.right.parent = nodesucc.parent

			if nodesuccisleftson: #understanding if the nodesucc gonna be left or right son
				originalparent.left = nodesucc
			else:
				originalparent.right = nodesucc

			nodesucc.parent = originalparent #repalce node by succs
			nodesucc.right = node.right
			nodesucc.left = node.left
			nodesucc.right.parent = nodesucc
			nodesucc.left.parent = nodesucc
		return originalparent

	def deletion_fix (self, node): #actually its get the parent, is it clear to write node?
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
		if (node is None) or (not node.is_real_node()):
			return []
		return self.avl_to_array_rec(node.left) + [(node.key, node.value)] + self.avl_to_array_rec(node.right)

	"""returns the number of items in dictionary 
	@rtype: int
	@returns: the number of items in dictionary 
	@post: returned integer is full size of the tree including the root
	"""
	def size(self):
		return self.root.size

	"""compute the rank of node in the dictionary

	@type node: AVLNode
	@pre: node is in self
	@param node: a node in the dictionary to compute the rank for
	@rtype: int
	@returns: the rank of node in self
	"""
	def rank(self, node):
		# FUNCTION NOT TESTED BECAUSE SIZE FIELD WAS NOT WORKING YET
		rank_sum = node.left.size + 1
		node_to_check = node
		while node_to_check is not None:
			if node_to_check == node_to_check.parent.right: # node_to_check is a right son
				rank_sum = rank_sum + node_to_check.parent.left.size + 1
			node_to_check = node_to_check.parent
		return rank_sum

	"""finds the i'th smallest item (according to keys) in the dictionary

	@type i: int
	@pre: 1 <= i <= self.size()
	@param i: the rank to be selected in self
	@rtype: AVLNode
	@returns: the node of rank i in self
	"""
	def select(self, i):
		# NOT TESTED BECAUSE SIZE FIELD DOES NOT WORK
		return self.select_rec(self.root, i)

	"""Recursively searches for the k'th smallest node in the dictionary
	@param node: current AVLNode
	@param k: the index of the node to be searched for
	@rtype: AVLNode
	@returns: the node of rank i in self
	"""
	def select_rec(self, node, k):
		# CHECK THIS FUNCTION WHEN SIZE FIELD WORKS
		r = node.left.size + 1
		if k == r:
			return node
		elif k < r:
			return self.select_rec(node.left, k)
		else:
			return self.select_rec(node.right, k-r)

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

		# TEST THIS UPDATE
		A.size = B.size
		B.size = B.check_size()

		B.height = B.check_height()
		A.height = A.check_height()

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

		# TEST THIS UPDATE
		A.size = B.size
		B.size = B.check_size()

		B.height = B.check_height()
		A.height = A.check_height()
		return None

	""" Function receives a node in the tree where BF has changed to |2| (AVL Criminal) and rotates LR
	@type node: AVLNode
	@param node: AVLNode where BF=2
	"""
	def left_then_right_rotation(self, node):
		B = node  # AVL criminal, original node
		parent = B.parent
		A = B.left  # left son of AVL criminal
		C = B.left.right  # node to become new root
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

		# TEST THIS UPDATE
		A.size = A.check_size()
		B.size = B.check_size()
		C.size = C.check_size()

		A.height = A.check_height()
		B.height = B.check_height()
		C.height = C.check_height()

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

		# TEST THIS UPDATE
		A.size = A.check_size()
		B.size = B.check_size()
		C.size = C.check_size()

		A.height = A.check_height()
		B.height = B.check_height()
		C.height = C.check_height()
		return None

	""" Method that receives a criminal AVLNode and conducts the correct rotation
	@pre: AVL_criminal is indeed a criminal (BF checked and BF = |2|)
	@type AVL_criminal: AVLNode
	@return: None
	"""
	def pick_rotation(self, AVL_criminal):

		criminal_bf = AVL_criminal.calculate_balance_factor()

		if criminal_bf == 2:
			son_bf = AVL_criminal.left.calculate_balance_factor()
			if son_bf == -1:
				self.left_then_right_rotation(AVL_criminal)
			else:
				self.right_rotation(AVL_criminal)
		else:
			son_bf = AVL_criminal.right.calculate_balance_factor()
			if son_bf == 1:
				self.right_then_left_rotation(AVL_criminal)
			else:
				self.left_rotation(AVL_criminal)




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

A = AVLTree()
key = input("Enter a new key: ")
while key != "-1":
	A.insert(int(key),key)
	printree(A.root)
	key = input("Enter a new key: ")


print(A.root.size)
print(A.root.height)

"""
B = AVLTree()
keys = [15,7,22,4,10,20,24,2,6,8,11,18,1,5,12]
for key in keys:
	B.insert(key,str(key))

printree(B.root)
print(B.size())
print(B.root.height)
"""