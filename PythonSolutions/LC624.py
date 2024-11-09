class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        lowest, secondLowest = arrays[0][-1], arrays[0][-1]
        lowestInd = secondLowestInd = 0
        highest, secondHighest = arrays[0][0], arrays[0][0]
        highestInd = secondHighestInd = 0
        for ind in range(len(arrays)):
            currentLow = arrays[ind][0]
            currentHigh = arrays[ind][-1]
            if currentLow <= lowest:
                secondLowest = lowest
                secondLowestInd = lowestInd
                lowest = currentLow
                lowestInd = ind
            elif currentLow < secondLowest:
                secondLowest = currentLow
                secondLowestInd = ind
            if currentHigh >= highest:
                secondHighest = highest
                secondHighestInd = highestInd
                highest = currentHigh
                highestInd = ind
            elif currentHigh > secondHighest:
                secondHighest = currentHigh
                secondHighestInd = ind
        if highestInd != lowestInd:
            return abs(highest - lowest)
        else:
            if abs(highest - secondHighest) < abs(lowest - secondLowest):
                return abs(secondHighest - lowest)
            else:
                return abs(highest - secondLowest)
