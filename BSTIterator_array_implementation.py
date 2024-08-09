from array import array


class _BSTMapIterator:
    def __init__(self, root, size):
        self._theKeys = array('i', [0]*size)
        self._currItem = 0
        self._bstTraversal(root)
        self._currItem = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._currItem < len(self._theKeys):
            key = self._theKeys[self._currItem]
            self._currItem += 1
            return key
        else:
            raise StopIteration

    def _bstTraversal(self, subtree):
        if subtree is not None:
            self._bstTraversal(subtree.left)
            self._theKeys[self._currItem] = subtree.key
            self._currItem += 1
            self._bstTraversal(subtree.right)

