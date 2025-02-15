# here's a memoized version (dp)
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        table = {0: 0}

        def dfs(targetChange):
            if targetChange in table:
                return table[targetChange]

            add = float("inf")
            for c in coins:
                if targetChange >= c:
                    add = min(add, dfs(targetChange - c))
            res = 1 + add
            if (
                targetChange in table and table[targetChange] > res
            ) or targetChange not in table:
                table[targetChange] = res
            return res

        dfs(amount)

        if table[amount] != float("inf"):
            return table[amount]
        else:
            return -1


# below is an even better soln:
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0
        # this works because we have a choice: for each coin, we either use one of those coins and we reduce the current amount by con
        # or we might not need to redo calculations at all, if we already have a dp value for this
        # iterate from coin to amount + 1 since we might have better ways to create certain change combos
        # ex/ coin = 1 amount = 10
        # dp[1] = dp[1] or dp[0] + 1
        # dp[2] = dp[2] or dp[1] + 1...
        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] = min(dp[x], dp[x - coin] + 1)
        return dp[amount] if dp[amount] != float("inf") else -1
