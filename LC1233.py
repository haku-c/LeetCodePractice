# Trie Refresher:
class Node:
    def __init__(self):
        self.children = {}
        self.end = False


class Trie:
    def __init__(self):
        self.root = Node()
        self.res = []

    def insert(self, wordList):
        current = self.root
        for i in range(len(wordList)):
            w = wordList[i]
            if w not in current.children:
                current.children[w] = Node()
            current = current.children[w]
        current.end = True

    def bfs(self, currentNode, currentString):
        if currentNode.end == True:
            self.res.append(currentString)
            return
        for key in currentNode.children:
            self.bfs(currentNode.children[key], currentString + "/" + key)

    def search(self):
        for key in self.root.children:
            self.bfs(self.root.children[key], "/" + key)


class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        trie = Trie()
        for i in range(len(folder)):
            path = folder[i]
            wordList = path.split("/")
            trie.insert(wordList[1:])
        trie.search()
        return trie.res


# there is an easier way to do this problem as follows:
# class Solution:
#     def removeSubFolders(self, folder):
#         folder.sort()
#         res = []
#         for path in folder:
#             # since we sort, the shorter paths with the same prefix will come before longer paths with the same prefix.
#             if not res or not path.startswith(res[-1] + "/"):
#                 res.append(path)
#         return res
