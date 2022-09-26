# --------------------------------- Suffix Trie --------------------------------

class Trie:
    """This is a conceptual class representation of Trie|
    This contains the following functions:|
    def __init__(self)|
    def find(self, root, c)|
    def insert(self, s)|
    def checkPrefix(self, s)|
    def countPrefix(self, s)|
        
    """
    
    def __init__(self):
        """Constructor defined.

        :param self: self means storing the provided information into created Trie
        :type self: Trie
        :Example:

        >>> from Trie import Trie
        >>> T = Trie()
        """
        self.T = {}
    
    def find(self, root, c):
        """Find function

        :param self: self means storing the provided information into created trie
        :type self: Trie
        :param root:root
        :type root:set
        :param c: c in root
        :type c:optional
        :return: c in root
        :rtype:optional
        :Example:

        >>> from Trie import Trie
        >>> T = Trie()
        >>> T.insert({1})
        >>> print(T.find(T.T,1))
        True
        """
    
        return (c in root)
    
    def insert(self, s):
        """Insert function.

        :param self: self means storing the provided information into created Trie
        :type self: Trie
        :param s: s
        :type s: optional
        :Example:

        >>> from Trie import Trie
        >>> T = Trie()
        >>> T.insert({1})
        """
        root = self.T
        for c in s:
            if not self.find(root,c):
                root[c] = {}
            root = root[c]
            root.setdefault('#',0)
            root['#'] += 1
    
    def checkPrefix(self, s):
        """CheckPrefix function.

        :param self: self means storing the provided information into created trie
        :type self: Trie
        :param s: s
        :type s: optional
        :Example:

        >>> from Trie import Trie
        >>> T = Trie()
        >>> T.insert({1})
        >>> print(T.checkPrefix({2}))
        False
        """
        root = self.T
        for idx, char in enumerate(s):
            if char not in root:
                if idx == len(s) - 1:    
                    root[char] = '#'
                else:
                    root[char] = {}
            elif root[char] == '#' or idx == len(s) - 1:
                return True
            root = root[char]
        return False
    
    def countPrefix(self, s):
        """countPrefix function.

        :param self: self means storing the provided information into created trie
        :type self: Trie
        :param s: s
        :type s: optional
        :Example:

        >>> from Trie import Trie
        >>> T = Trie()
        >>> T.insert({1})
        >>> T.insert({2})
        >>> T.insert({2})
        >>> print(T.countPrefix({2}))
        2
        """
        found = True
        root = self.T
        for c in s:
            if self.find(root,c):
                root = root[c]
            else:
                found = False
                break
        if found:
            return root['#']
        return 0