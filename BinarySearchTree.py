# -------------------------- Binary Search Tree ------------------------------


class BSTNode:
    """This is a conceptual class representation of BSTNode.|
    This contains the following functions:|
    def __init__(self,info)|
    def __str__(self)|

    """
    
    def __init__(self, info):
        """Constructor defined.

        :param self: self means storing the provided information into created heap
        :type self: Heap
        :param info: info
        :type info: optional
        :Example:

        >>> from BinarySearchTree import BSTNode
        >>> B = BSTNode(20)
        """
        self.info = info
        self.left = None
        self.right = None
        self.level = None
    
    def __str__(self):
        """Converter to string.

        :return: str(self.info)
        :rtype: str
        :Example:

        >>> from BinarySearchTree import BSTNode
        >>> B = BSTNode("hello")
        >>> print(B.__str__())
        hello
        """
        return str(self.info)

class BinarySearchTree:
    """This is a conceptual class representation of BinarySearchTree.|
    This contains the following functions:|
    def __init__(self)|
    def insert(self, val)|
    def traverse(self, order)|
    def height(self, root)|

    """
    
    def __init__(self):
        """Constructor defined.

        :param self: self means storing the provided information into created heap
        :type self: Heap
        :Example:

        >>> from BinarySearchTree import BinarySearchTree
        >>> B = BinarySearchTree()
        """
        self.root = None
    
    def insert(self, val):
        """Insert function.

        :param self: self means storing the provided information into created heap
        :type self: Heap
        :param val: val
        :type val: optional
        :Example:

        >>> from BinarySearchTree import BinarySearchTree
        >>> B = BinarySearchTree()
        >>> B.insert(2)
        >>> B.insert(1)
        """
        if self.root == None:
            self.root = BSTNode(val)
        else:
            current = self.root
            while True:
                if val < current.info: # move to left sub-tree
                    if current.left:
                        current = current.left # root moved
                    else:
                        current.left = BSTNode(val) # left init
                        break
                elif val > current.info: # move to right sub-tree
                    if current.right:
                        current = current.right # root moved
                    else:
                        current.right = BSTNode(val) # right init
                        break
                else:
                    break # value exists
    
    def traverse(self, order):
        """Traverse function.

        :param self: self means storing the provided information into created heap
        :type self: Heap
        :param order: order
        :type order: optional
        :Example:

        >>> from BinarySearchTree import BinarySearchTree
        >>> B = BinarySearchTree()
        >>> B.insert(1)
        >>> B.insert(2)
        >>> B.insert(3)
        >>> B.traverse('PRE')
        1 2 3 
        """
        def preOrder(root):
            print(root.info, end = ' ')
            if root.left != None:
                preOrder(root.left)
            if root.right != None:
                preOrder(root.right)
        def inOrder(root):
            if root.left != None:
                inOrder(root.left)
            print(root.info, end = ' ')
            if root.right != None:
                inOrder(root.right)
        def postOrder(root):
            if root.left != None:
                postOrder(root.left)
            if root.right != None:
                postOrder(root.right)
            print(root.info, end = ' ')
        if order == 'PRE':
            preOrder(self.root)
        elif order == 'IN':
            inOrder(self.root)
        elif order == 'POST':
            postOrder(self.root)
    
    def height(self, root):
        """Height function.

        :param self: self means storing the provided information into created heap
        :type self: Heap
        :param root: val
        :type root: optional
        :return: height
        :rtype: int
        :Example:

        >>> from BinarySearchTree import BinarySearchTree
        >>> B = BinarySearchTree()
        >>> B.insert(1)
        >>> B.insert(2)
        >>> B.insert(3)
        >>> print(B.height(B.root))
        2
        """
        if root.left == None and root.right == None:
            return 0
        elif root.right == None:
            return 1 + self.height(root.left)
        elif root.left == None:
            return 1 + self.height(root.right)
        else:
            return 1 + max(self.height(root.left),self.height(root.right))