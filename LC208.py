# class TrieNode:
#     def __init__(self):
#         children = None * 26
#         wordEnd = 0


# version of the trie or prefix tree
# class Trie:

#     def __init__(self):
#         self.children = [None] * 26
#         self.wordEnd = 0

#     def insert(self, word: str) -> None:
#         current = self
#         for c in word:
#             ind = ord(c) - 97
#             if current.children[ind] is not None:
#                 current = current.children[ind]
#             else:
#                 nxt = Trie()
#                 current.children[ind] = nxt
#                 current = nxt
#         current.wordEnd = 1

#     def search(self, word: str) -> bool:
#         current = self
#         for c in word:
#             ind = ord(c) - 97
#             if current.children[ind] is not None:
#                 current = current.children[ind]
#             else:
#                 return False
#         if current.wordEnd:
#             return True
#         return False


#     def startsWith(self, prefix: str) -> bool:
#         current = self
#         for c in prefix:
#             ind = ord(c) - 97
#             if current.children[ind] is not None:
#                 current = current.children[ind]
#             else:
#                 return False
#         return True
# a different version using a class for nodes and hashmap for children.
class TrieNode:
    def __init__(self):
        self.children = {}
        self.wordEnd = False


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        current = self.root
        for c in word:
            if c not in current.children:
                current.children[c] = TrieNode()
                current = current.children[c]
            else:
                current = current.children[c]
        current.wordEnd = 1

    def search(self, word: str) -> bool:
        current = self.root
        for c in word:
            if c in current.children:
                current = current.children[c]
            else:
                return False
        if current.wordEnd:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        current = self.root
        for c in prefix:
            if c in current.children:
                current = current.children[c]
            else:
                return False
        return True
