class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0 
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root
        for c in word:
            if c not in current.children:
                current.children[c] = TrieNode()
            current = current.children[c]
            current.count += 1
    
    def find(self, word):
        current = self.root
        value = 0
        for c in word:
            current = current.children[c]
            value += current.count
        return value 

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        n = len(words)
        res = [0] * n
        trie = Trie()
        for w in words:
            trie.insert(w)

        for i in range(n):
            res[i] = trie.find(words[i])

        return res
