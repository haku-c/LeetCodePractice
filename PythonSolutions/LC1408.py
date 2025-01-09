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
            # increment everytime we encounter this node since we want to build up substrings from suffixes (allowing the substrings of what we insert to count)
            current.count += 1

    def find(self, word):
        current = self.root
        for c in word:
            current = current.children[c]

        return current.count > 1


class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        trie = Trie()
        # insert every single possible substring of the words.
        # notice how if we insert just the suffixes, we still get all substrings:
        # inserting abc effectively inserts a, ab, abc into the trie
        # inserting bc inserts bc
        # inserting c inserts c
        for word in words:
            for i in range(len(word)):
                trie.insert(word[i:])
        res = []
        for word in words:
            if trie.find(word):
                res.append(word)
        return res


# this is the trie solution.
