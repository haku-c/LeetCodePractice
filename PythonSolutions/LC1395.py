def numTeams(self, rating: List[int]) -> int:
    n = len(rating)
    opt = [0] * n
    greater = [0] * n
    less = [0] * n
    for i in range(1, n):
        g = 0
        l = 0
        for j in range(i):
            if rating[j] < rating[i]:
                g += 1
            else:
                l += 1
        greater[i] = g
        less[i] = l
    for i in range(2, n):
        end = rating[i]
        count = 0
        for j in range(1, i):
            if end > rating[j]:
                count += greater[j]
            else:
                count += less[j]
        opt[i] = count

    return sum(opt)


# O(2n^2):
# 2 parts of the algorithm: construct a table less and greater where less[i] is the number of elements 0 < j < i such that
# rating[i] < rating[j]. greater is similar w/ rating[i] > rating[j]
# then when we traverse through the soldier list again, we can use greater and less to add together the number of combinations where the current soldier is the third soldier in the combination
# if rating[i] > rating[j] then we can have all combinations where there exists some k such that rating[k] < rating[j] < rating[i]. this is tracked in grater[j]
# the opt table is opt[i] = # valid combinations ending with soldier i
# sum the table for the final answer
# one runtime note: you can get faster runtime if you assign temp variables to hold the counts in the loops instead of accessing greater[i], less[i] or opt[i] and updating
