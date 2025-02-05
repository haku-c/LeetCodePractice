import bisect
from collections import defaultdict


class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    # O(n) inserts
    def set(self, key: str, value: str, timestamp: int) -> None:
        bisect.insort(self.store[key], (timestamp, value))

    # O(logn) gets
    def get(self, key: str, timestamp: int) -> str:
        lst = self.store[key]
        # if there is no key entry, return ""
        if lst == []:
            return ""
        index = bisect.bisect_left(lst, (timestamp, ""))
        # if we have a match timestamp, return the match
        if index != (len(lst)) and lst[index][0] == timestamp:
            return lst[index][1]
        # if we don't have a match, but an existing prior timestamp is less than, return the prior
        elif lst[index - 1][0] < timestamp:
            return lst[index - 1][1]
        # if everything is greater, return ""
        else:
            return ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
