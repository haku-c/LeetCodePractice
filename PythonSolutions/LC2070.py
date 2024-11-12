class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort(key=lambda x: x[0])
        currentMaxBeauty = 0
        for i in range(len(items)):
            price, beauty = items[i]
            currentMaxBeauty = max(currentMaxBeauty, beauty)
            items[i][1] = currentMaxBeauty

        # if you use start < end then after the loop you need to check if items[start][0] works or not since you never checked it in the loop
        # in the future, prefer using start <= end.
        # def search(price):
        #     start = 0
        #     end = len(items) - 1
        #     while start < end:
        #         mid = start + (end - start) // 2
        #         if items[mid][0] > price:
        #             end = mid - 1
        #         else:
        #             start = mid + 1
        #     if items[start][0] <= price:
        #         return items[start][1]
        #     elif start > 0:
        #         return items[start - 1][1]
        #     else:
        #         return 0

        # the cleaner binary search solution is below
        def search(price):
            start = 0
            end = len(items) - 1
            result = 0
            while start <= end:
                mid = start + (end - start) // 2
                if items[mid][0] > price:
                    end = mid - 1
                else:
                    result = max(result, items[start][1])
                    start = mid + 1
            return result

        res = []
        for query in queries:
            r = search(query)
            res.append(r)
        return res
