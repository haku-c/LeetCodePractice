# There are  N dishes in a row on a kaiten belt, with the # ith dish being of type D_i
# Some dishes may be of the same type as one another.
# You're very hungry, but you'd also like to keep things interesting. The N dishes will arrive in front of you,
# one after another in order, and for each one you'll eat it as long as it isn't the same type as any of the previous K dishes you've eaten.
# You eat very fast, so you can consume a dish before the next one gets to you.
# Any dishes you choose not to eat as they pass will be eaten by others.
# Determine how many dishes you'll end up eating.

from typing import List

# Write any import statements here
from collections import deque


def getMaximumEatenDishCount(N: int, D: List[int], K: int) -> int:
    # Write your code here
    lastK = deque()
    seen = set()
    res = 0
    for i in range(N):
        currentType = D[i]
        if currentType in seen:
            continue
        else:
            seen.add(currentType)
            lastK.append(currentType)
            if len(lastK) > K:
                old = lastK.popleft()
                seen.remove(old)
            res += 1
    return res


# use a deque for constant time removal from the front and the end of the last Kth eaten items
# use a set to track which items you have eaten in the last k
