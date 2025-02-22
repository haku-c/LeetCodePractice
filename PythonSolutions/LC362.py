import bisect


class HitCounter:

    def __init__(self):
        self.times = []

    def hit(self, timestamp: int) -> None:
        self.times.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        start = 0
        end = len(self.times) - 1
        target = timestamp - 299
        left = bisect.bisect_left(self.times, target)
        right = bisect.bisect_right(self.times, timestamp)
        return right - left


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)

# alternate approach is to use a deque and pop from the front if the timestamp is less than the window minimum.
# since the window can be at max 300 entries long, it's constant time amortized
# ^ using clustering where we have a pair, (key, val) where key is the timestamp and val is the number of appearances of key
# since everything is increasing, it's easy to update the queue.
