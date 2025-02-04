class Solution:
    def intervalIntersection(
        self, firstList: List[List[int]], secondList: List[List[int]]
    ) -> List[List[int]]:

        aTrack = 0
        bTrack = 0
        m = len(firstList)
        n = len(secondList)
        res = []
        while aTrack < m and bTrack < n:
            aStart, aEnd = firstList[aTrack]
            bStart, bEnd = secondList[bTrack]
            # if disjoint intervals
            if bEnd < aStart:
                bTrack += 1
            elif aEnd < bStart:
                aTrack += 1
            # limits are not disjoint
            elif aStart <= bStart:
                if aEnd < bEnd:
                    res.append([bStart, aEnd])
                    aTrack += 1
                else:
                    res.append([bStart, bEnd])
                    bTrack += 1
            elif bStart <= aStart:
                if aEnd < bEnd:
                    res.append([aStart, aEnd])
                    aTrack += 1
                else:
                    res.append([aStart, bEnd])
                    bTrack += 1
        return res


# straightforward linear approach, just make sure to do some case analysis
