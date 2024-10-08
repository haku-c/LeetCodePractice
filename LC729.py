class MyCalendar:
    def __init__(self):
        self.blocked = set()

    def book(self, start: int, end: int) -> bool:
        for currentStart, currentEnd in self.blocked:
            if not (start >= currentEnd or end <= currentStart):
                return False
        self.blocked.add((start, end))
        return True


# iterating through the items in a sorted manner would allow you to reduce the number of checks to just the values in the closest
# intervals
# class MyCalendar:

#     def __init__(self):
#         self.calendar = []

#     def book(self, start: int, end: int) -> bool:
#         # Find the position to insert the new event using binary search
#         i = bisect_left(self.calendar, (start, end))

#         # Check for overlap with the previous event
#         if i > 0 and self.calendar[i - 1][1] > start:
#             return False

#         # Check for overlap with the next event
#         if i < len(self.calendar) and end > self.calendar[i][0]:
#             return False

#         # Insert the new event if no overlaps
#         self.calendar.insert(i, (start, end))
#         return True
