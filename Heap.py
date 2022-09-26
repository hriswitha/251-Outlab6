# ------------------------heap.py------------------------

class Heap:
    """This is a conceptual class representation of heap.|
    This contains the following functions:|
    def __init__(self, cap)|
    def parent(self, i)|
    def left(self, i)|
    def right(self, i)|
    def insert(self, val)|
    def min(self)|
    def Heapify(self, root)|
    def deleteMin(self)|
    """
    
    def __init__(self, cap):
        """Constructor defined.

        :param self: self means storing the provided information into created heap
        :type self: Heap
        :param cap: max no of parameter to store in heap
        :type cap: optional 
        :Example:

        >>> from Heap import Heap
        >>> H = Heap(20)            
        """
        self.H = []
        self.n = 0
        self.M = cap
    
    def parent(self, i):
        """Parent function.

        :param self: self stores the info given to heap created
        :type self: Heap
        :param i: input
        :type i: int
        :return: a value int((i-1)/2)
        :rtype: int
        :Example:

        >>> from Heap import Heap
        >>> H = Heap(20)
        >>> H.insert(1)
        >>> H.insert(2)
        >>> print(H.parent(3))
        1
    	"""
        return (i - 1) //2
    
    def left(self, i):
        """Left function.

        :param self: self stores the info given to heap created
        :type self: Heap
        :param i: input
        :type i: int
        :return: a value (2*i)+1
        :rtype: int
        :Example:

        >>> from Heap import Heap
        >>> H = Heap(20)
        >>> H.insert(1)
        >>> H.insert(2)
        >>> print(H.left(2))
        5
    	"""
        return (2 * i) + 1
    
    def right(self, i):
        """Right function.

        :param self: self stores the info given to heap created
        :type self: Heap
        :param i: input
        :type i: int
        :return: a value 2*(i+1)
        :rtype: int
        :Example:

        >>> from Heap import Heap
        >>> H = Heap(20)
        >>> H.insert(1)
        >>> H.insert(2)
        >>> print(H.right(2))
        6
    	"""
        return 2 * (i + 1)
    
    def insert(self, val):
        """Inserts value into the heap.

        :param self: self stores the info given to heap created
        :type self: Heap
        :param val: index input value
        :type val: int
        :Example:

        >>> from Heap import Heap
        >>> H = Heap(20)
        >>> H.insert(2)

        """
        if self.n != self.M:
            self.H.append(val)
            i = self.n
            self.n += 1
            while i != 0 and self.H[self.parent(i)] > self.H[i]:
                self.H[i], self.H[self.parent(i)] = self.H[self.parent(i)], self.H[i]
                i = self.parent(i)
    
    def min(self):
        """Returns the min of heap .

        :param self: self stores the info given to heap created
        :type self: Heap
        :return: a value self.H[0] or -1
        :rtype: int
        :Example:

        >>> from Heap import Heap
        >>> H = Heap(20)
        >>> H.insert(1)
        >>> H.insert(2)
        >>> H.insert(3)
        >>> print(H.min())
        1
        """
        if (self.n != 0):
            return self.H[0]
        return -1
    
    def Heapify(self, root):
        """Creates heapify.

        :param self: self stores the info given to heap created
        :type self: Heap
        :param root: Used to call left, right
        :type root: int
        :Example:

        >>> from Heap import Heap
        >>> L = Heap(20)
        >>> L.insert(1)
        >>> L.insert(2)
        >>> L.insert(3)
        >>> print(L.Heapify(1))
        None
        """
        l = self.left(root)
        r = self.right(root)
        s = root
        if (l < self.n and self.H[l] < self.H[root]):
            s = l
        if (r < self.n and self.H[r] < self.H[s]):
            s = r
        if s != root:
            self.H[root], self.H[s] = self.H[s], self.H[root]
            self.Heapify(s)
    
    def deleteMin(self):
        """Deletes min element.
        :Example:

        >>> from Heap import Heap
        >>> H = Heap(20)
        >>> H.insert(1)
        >>> H.insert(2)
        >>> H.insert(3)
        >>> H.deleteMin()
        >>> print(H.min())
        2
        """
        if self.n > 0:
            if self.n == 1:
                self.H = []
                self.n = 0
            else:
                self.n -= 1
                self.H[0] = self.H[self.n]
                self.Heapify(0)