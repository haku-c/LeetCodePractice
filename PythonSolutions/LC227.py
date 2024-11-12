import re


class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(" ", "")
        nums = re.split("[+-/*]", s)
        nums = list(map(int, nums))
        ops = "".join(re.split("[0-9]+", s))
        eqn = [nums[0]]
        for index in range(len(ops)):
            op = ops[index]
            if op == "*":
                left = eqn.pop()
                right = nums[index + 1]
                eqn.append(left * right)
            elif op == "/":
                left = eqn.pop()
                right = nums[index + 1]
                eqn.append(int(left / right))
            else:
                eqn.append(nums[index + 1])
        index = 1
        res = eqn[0]
        for op in ops:
            if op == "+":
                res = res + eqn[index]
                index += 1
            elif op == "-":
                res = res - eqn[index]
                index += 1
        return res


# this approach uses a stack, but there is a better way without the stack (do the operations in order and only save the left operand). Also, we can construct the numbers as we go...
