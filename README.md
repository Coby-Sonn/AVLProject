# AVL Tree Implementation 🌳

This project implements an AVL tree data structure in Python. The AVL tree is a self-balancing binary search tree where the difference in heights between the left and right subtrees for any node is at most one (|node.balance_factor|<=1). This ensures efficient insertion, deletion, and lookup operations.

The attached code was built with a fellow student as part of our studies during Tel Aviv University's Data Structures course 🎓

While working on this project, we focused on writing clean, clear, and efficient code, alongside implementing correct and efficient algorithms to ensure the best possible runtime for the multiple methods within the implementation. 🚀💻

## 📖 Features
✅ **Insertion** (`insert(key, value)`) - Adds a new key-value pair to the AVL tree while maintaining balance.  
✅ **Deletion** (`delete(node)`) - Removes a node from the tree while rebalancing if necessary.  
✅ **Search** (`search(key)`) - Retrieves a node by its key in O(log n) time.  
✅ **Balance Factor Calculation** - Ensures the tree maintains the AVL property.  
✅ **Successor & Predecessor Lookup** - Allows for efficient in-order traversal.  
✅ **Rank & Select** (`rank(node)`, `select(i)`) - Retrieves the rank of a node and selects the i-th smallest node.  
✅ **Max in Range** (`max_range(a, b)`) - Finds the node with the highest value within a given key range.  
✅ **Array Representation** (`avl_to_array()`) - Converts the AVL tree into a sorted list of (key, value) pairs.  

### You can interact with the AVL tree in a Python environment:

```python
from avl_tree import AVLTree

# Create an AVL Tree
tree = AVLTree()

# Insert elements
tree.insert(10, "Ten")
tree.insert(20, "Twenty")
tree.insert(30, "Thirty")

# Search for a key
node = tree.search(20)
print(node.value if node else "Key not found")

# Delete a node
tree.delete(node)
