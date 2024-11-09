def averageWaitingTime(self, customers: List[List[int]]) -> float:
    waiting = 0
    currentTime = customers[0][0]
    for arrival, timeTaken in customers:
        if currentTime >= arrival:
            currentTime += timeTaken
        else:
            currentTime = arrival
            currentTime += timeTaken
        waiting += currentTime - arrival
    return waiting / len(customers)


# there are 2 scenarios:
# 1. you wait for the next customer to arrive (currentTime<arrival)
# 2. the next customer has already arrived.
