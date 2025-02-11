import random


class RandomizedSet:

    def __init__(self):
        self.s = {}
        self.l = []

    def insert(self, val: int) -> bool:
        if val in self.s:
            return False
        # s.val represents the index in the list we keep the key representative for the set
        self.s[val] = len(self.l)
        self.l.append(val)
        return True

    def remove(self, val: int) -> bool:
        # we always remove from the end of the list in constant time.
        # so we want to swap the item that we are removing with the last item in the list
        # get the last item, get the index in the list to move that item to
        if val in self.s:
            newElement, indexMoveTo = self.l[-1], self.s[val]
            # don't forget to also change the index we stored in the dictionary so you can index into the list correctly
            self.l[indexMoveTo], self.s[newElement] = newElement, indexMoveTo
            self.l.pop()
            del self.s[val]
            return True
        return False

    def getRandom(self) -> int:
        # this is faster than iterating in to the list with a random integer
        return choice(self.l)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
