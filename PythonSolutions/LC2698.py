class Solution:
    def punishmentNumber(self, n: int) -> int:
        def check(number, target, start, startingSum):
            if startingSum > target:
                return False
            # if the sum of the partitions and the last partition matches
            if startingSum + int(number[start:]) == target:
                return True

            currentSum = startingSum
            for index in range(start + 1, len(number)):
                # add partition
                if check(number, target, index, currentSum + int(number[start:index])):
                    return True
                # remove partition

            return False

        res = 0
        for i in range(1, n + 1):
            if check(str(i**2), i, 0, 0):
                # print(i)
                res += i**2

        return res


# backtracking solution
# you can improve runtime w/o converting and using modulo
class Solution:
    def can_partition(self, num, target):
        # Invalid partition found
        if target < 0 or num < target:
            return False

        # Valid partition found
        if num == target:
            return True

        # Recursively check all partitions for a valid partition

        # target == n, 1<=n<=1000, so these are the 3 choices
        return (
            self.can_partition(num // 10, target - num % 10)
            or self.can_partition(num // 100, target - num % 100)
            or self.can_partition(num // 1000, target - num % 1000)
        )

    def punishmentNumber(self, n: int) -> int:
        punishment_num = 0

        # Iterate through numbers in range [1, n]
        for current_num in range(1, n + 1):
            square_num = current_num * current_num

            # Check if valid partition can be found and add squared number if so
            if self.can_partition(square_num, current_num):
                punishment_num += square_num

        return punishment_num
