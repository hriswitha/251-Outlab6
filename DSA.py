################################## Data Structures ################################

# ------------------------------- Singly Linked List -----------------------------

class SinglyLinkedListNode:
    """This is a conceptual class representation of SinglyLinkedListNode.|
    This contains the following functions:|
    def __init__(self, data)|
    def __str__(self)|

    """

    def __init__(self, data):
        """Constructor defined.

        :param self: self means storing the provided information into created heap.
        :type self: Heap
        :param data: data
        :type data: optional
        :Example:

        >>> from DSA import SinglyLinkedListNode
        >>> S = SinglyLinkedListNode(20)
        """
        self.data = data
        self.next = None
    
    def __str__(self):
        """Converter to string.

        :return: str(self.data)
        :rtype: str
        :Example:

        >>> from DSA import SinglyLinkedListNode
        >>> S = SinglyLinkedListNode("hello")
        >>> print(S.__str__())
        hello
        """
        return str(self.data)

class SinglyLinkedList:
    """This is a conceptual class representation of SinglyLinkedList.|
    This contains the following functions:|
    def __init__(self)|
    def insert(self, data)|
    def find(self, data)|
    def deleteVal(self, data)|
    def printer(self, sep = ', ')|
    def reverse(self)|

    """
    
    def __init__(self):
        """Constructor defined.

        :param self: self means storing the provided information into created heap
        :type self: Heap
        :Example:

        >>> from DSA import SinglyLinkedList
        >>> S = SinglyLinkedList()
        """
        self.head = None
        self.tail = None
   
    def insert(self, data):
        """Insert function.

        :param self: self means storing the provided information into created heap
        :type self: Heap
        :param data: data
        :type data: optional
        :Example:

        >>> from DSA import SinglyLinkedList
        >>> S = SinglyLinkedList()
        >>> S.insert(1)
        """
        node = SinglyLinkedListNode(data) # new node
        if not self.head: # no head
            self.head = node
        else:
            self.tail.next = node # add behind tail
        self.tail = node # move tail
    
    def find(self, data):
        """Find function.

        :param self: self means storing the provided information into created heap
        :type self: Heap
        :param data: data
        :type data: optional
        :return: a node with given input data
        :rtype: SingleLinkedListNode
        :Example:

        >>> from DSA import SinglyLinkedList
        >>> S = SinglyLinkedList()
        >>> S.insert(1)
        >>> S.insert(2)
        >>> L = S.find(2)
        >>> print(L.__str__())
        1
        """
        head = self.head
        prev = None
        while head != None and head.data != data:
            prev = head
            head = head.next
        return prev
    
    def deleteVal(self, data):
        """Delete function.

        :param self: self means storing the provided information into created heap
        :type self: Heap
        :param data: data
        :type data: optional
        :return: True
        :return: False
        :rtype: bool
        :Example:

        >>> from DSA import SinglyLinkedList
        >>> S = SinglyLinkedList()
        >>> S.insert(1)
        >>> S.insert(2)
        >>> S.deleteVal(2)
        True
        """
        prevPos = self.find(data)
        if prevPos.next == None:
            return False
        prevPos.next.next = prevPos.next
        return True
    
    def printer(self, sep = ', '):
        """Printer function.

        :param self: self means storing the provided information into created heap
        :type self: Heap
        :param sep: separator
        :type sep: str
        :Example:

        >>> from DSA import SinglyLinkedList
        >>> S = SinglyLinkedList()
        >>> S.insert(1)
        >>> S.insert(2)
        >>> S.printer()
        [1, 2]
        """
        ptr = self.head
        print('[', end = '')
        while ptr != None:
            print(ptr, end = '')
            ptr = ptr.next
            if ptr != None:
                print(sep, end = '')
        print(']')
    
    def reverse(self):
        """Reverse function.

        :param self: self means storing the provided information into created heap
        :type self: Heap
        :Example:

        >>> from DSA import SinglyLinkedList
        >>> S = SinglyLinkedList()
        >>> S.insert(1)
        >>> S.insert(2)
        >>> S.reverse()
        >>> S.printer()
        [2, 1]
        """
        head = self.head # head pointer
        prev = None # previous pointer
        while head != None: # while there is forward link left
            newHead = head.next # save extra pointer to next element
            head.next = prev # reverse the link of current element
            prev = head # move pointer to previous element
            head = newHead # use extra pointer to move to next element
        self.tail = self.head
        self.head = prev


def merge(list1, list2):
    """Merge function of 2lists.

    :param list1: input list 1
    :type list1: list
    :param list1: input list 1
    :type list1: list
    :return: merged list
    :rtype: SinglyLinkedList
    :Example:

        >>> from DSA import merge
        >>> from DSA import SinglyLinkedList
        >>> L1 = SinglyLinkedList()
        >>> L1.insert(1)
        >>> L1.insert(2)
        >>> L2 = SinglyLinkedList()
        >>> L2.insert(3)
        >>> L2.insert(4)
        >>> merge(L1,L2).printer()
        [1, 2, 3, 4]
    """
    merged = SinglyLinkedList()
    head1 = list1.head
    head2 = list2.head
    while head1 != None and head2 != None: # both lists not empty
        if head1.data < head2.data: # link node with smaller data
            merged.insert(head1.data)
            head1 = head1.next
        else:
            merged.insert(head2.data)
            head2 = head2.next
    if head1 == None and head2 != None: # list 1 finished
        merged.tail.next = head2 # add remaining list 2 as is
    if head1 != None and head2 == None: # list 2 finished
        merged.tail.next = head1 # add remaining list 1 as is
    return merged

# ------------------------------ Doubly Linked List ----------------------------

class DoublyLinkedListNode:
    """This is a conceptual class representation of SinglyLinkedList.|
    This contains the following functions:|
    def __init__(self, data)|
    def __str__(self)|

    """
    
    def __init__(self, data):
        """Constructor defined

        :param self: self means storing the provided information into created heap
        :type self: Heap
        :param data: data
        :type data: optional
        :Example:

        >>> from DSA import DoublyLinkedListNode
        >>> D = DoublyLinkedListNode(1)
        
        """
        self.data = data
        self.next = None
        self.prev = None
    
    def __str__(self):
        """Converter to string

        :return: str(self.data)
        :rtype: str
        :Example:

        >>> from DSA import DoublyLinkedListNode
        >>> D = DoublyLinkedListNode("hello")
        >>> print(D.__str__())
        hello
        """
        return str(self.data) 

class DoublyLinkedList:
    """This is a conceptual class representation of DoublyLinkedList.|
    This contains the following functions:|
    def __init__(self)|
    def insert(self, data)|
    def printer(self, sep = ', ')|
    def reverse(self)|

    """

    
    def __init__(self):
        """Constructor defined.

        :param self: self means storing the provided information into created heap
        :type self: Heap
        :param data: data
        :type data: optional
        :Example:

        >>> from DSA import DoublyLinkedList
        >>> D = DoublyLinkedList()
        """
        self.head = None
        self.tail = None
    
    def insert(self, data):
        """Insert function.

        :param self: self means storing the provided information into created heap
        :type self: Heap
        :param data: data
        :type data: optional
        :Example:

        >>> from DSA import DoublyLinkedList
        >>> D = DoublyLinkedList()
        >>> D.insert(1)
        >>> D.insert(2)
        """
        node = DoublyLinkedListNode(data) # new node
        if not self.head: # no head
            self.head = node
        else:
            self.tail.next = node # add behind tail
            node.prev = self.tail
        self.tail = node # move tail
    
    def printer(self, sep = ', '):
        """Printer function.

        :param self: self means storing the provided information into created heap
        :type self: Heap
        :param sep: separator
        :type sep: str
        :Example:

        >>> from DSA import DoublyLinkedList
        >>> D = DoublyLinkedList()
        >>> D.insert(2)
        >>> D.insert(1)
        >>> D.printer()
        [2, 1]
        """
        ptr = self.head
        print('[', end = '')
        while ptr != None:
            print(ptr, end = '')
            ptr = ptr.next
            if ptr != None:
                print(sep, end = '')
        print(']')
    
    def reverse(self):
        """Reverse function.

        :param self: self means storing the provided information into created heap
        :type self: Heap
        :Example:

        >>> from DSA import DoublyLinkedList
        >>> D = DoublyLinkedList()
        >>> D.insert(1)
        >>> D.insert(2)
        >>> D.reverse()
        >>> D.printer()
        [2, 1]
        """
        head = self.head # head pointer
        prev = None # previous pointer
        while head != None: # new node left
            newHead = head.next # save pointer to next node (cut forward link)
            if newHead != None: # check if next node has a reverse link
                newHead.prev = head # save pointer to previous node (cut reverse link)
            head.next = prev # reverse the forward link
            head.prev = newHead # reverse the reverse link
            prev = head # move pointer to previous element
            head = newHead # use saved pointer to move head
        self.tail = self.head
        self.head = prev






