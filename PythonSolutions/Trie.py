class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root
        for letter in range(word):
            if letter not in current.children:
                current.children[letter] = TrieNode()
            current = current.children[letter]
        current.end = True

    def find(self, word):
        current = self.root
        for letter in range(word):
            if letter in current.children:
                current = current.children[letter]
            else:
                return False
        return current.end
