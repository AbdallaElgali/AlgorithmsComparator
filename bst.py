from BSTIterator_array_implementation import _BSTMapIterator

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None


class BSTMap:
        def __init__(self):
            self.root = None
            self.size = 0

        def len(self):
            return self.size

        def __iter__(self):
            return _BSTMapIterator(self.root, self.len())

        def __contains__(self, key):
            return self._bstSearch(self.root, key)

        def getValue(self, key):
            node = self._bstSearch(self.root, key)
            assert node is not None
            return node.value

        def _bstSearch(self, subtree, key):
            if subtree is None:
                return None

            elif subtree.key > key:
                return self._bstSearch(subtree.left, key)

            elif subtree.key < key:
                return self._bstSearch(subtree.right, key)

            return subtree

        def minValue(self):
            min = self._minValue(self.root)
            return min

        def _minValue(self, subtree):
            if subtree is None:
                return None
            elif subtree.left is None:
                return subtree
            else:
                return self._minValue(subtree.left)

        def maxValue(self):
            max = self._maxValue(self.root)
            return max

        def _maxValue(self, subtree):
            if subtree is None:
                return None
            elif subtree.right is None:
                return subtree
            else:
                return self._minValue(subtree.right)


        def insert(self, key, value):
            node = self._bstSearch(self.root, key)
            if node is not None:
                node.value = value
                return False

            else:
                self.root = self._bstInsert(self.root, key, value)
                self.size += 1
                return True

        def _bstInsert(self, subtree, key, value):
            if subtree is None:
                return Node(key, value)
            elif key < subtree.key:
                subtree.left = self._bstInsert(subtree.left, key, value)
            elif key > subtree.key:
                subtree.left = self._bstInsert(subtree.right, key, value)

            return subtree

        def delete(self, key):
            self.root = self._bstDelete(self.root, key)
            self.size -= 1

        def _bstDelete(self, subtree, key):

            # Find the node to be deleted
            if subtree is None:
                return subtree
            elif key < subtree.key:
                subtree.left = self._bstDelete(subtree.left, key)
                return subtree
            elif key > subtree.key:
                subtree.right = self._bstDelete(subtree.right, key)
                return subtree

            else:
                # Case no.1: Leaf Node
                if subtree.left is None and subtree.right is None:
                    return None

                # Case no.2: 1 child
                elif subtree.left is None or subtree.right is None:
                    if subtree.right is None:
                        return subtree.left
                    else:
                        return subtree.right

                else:
                    successor = self._minValue(subtree.right)
                    subtree.key, subtree.value = successor.key, successor.value
                    subtree.right = self._bstDelete(subtree.right, successor.key)
                    return subtree

