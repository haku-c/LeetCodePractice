from collections import defaultdict


class MyCalendarTwo:

    def __init__(self):
        self.counts = defaultdict(int)

    def book(self, startTime: int, endTime: int) -> bool:
        self.counts[startTime] += 1
        self.counts[endTime] -= 1
        temp = sorted(self.counts.items())
        c = 0
        for _, count in temp:
            c += count
            if c > 2:
                self.counts[startTime] -= 1
                self.counts[endTime] += 1

                if self.counts[startTime] == 0:
                    del self.counts[startTime]

                return False

        return True


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(startTime,endTime)

# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(startTime,endTime)

# line sweep version (a bit slow since we resort in every query)
