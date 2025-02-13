import timeit


# standard backtracking solution. we assign the array at that index to a certain value and then recurse.
# don't forget to undo the assignment after recursion
class Solution:
    def countArrangement(self, n: int) -> int:
        self.res = 0

        # just check if your index got to the end
        def recurse(index, arr):
            if index == n + 1:
                self.res += 1
                return
            for i in range(1, n + 1):
                if not arr[i] and (i % index == 0 or index % i == 0):
                    arr[i] = 1
                    recurse(index + 1, arr)
                    arr[i] = 0

        recurse(1, [0] * (n + 1))
        return self.res


# apparently counting is the fastest of the three methods
def f():
    lst = [1] * 15
    return sum(lst)


def f2():
    lst = [1] * 15
    return lst.count(1)


def f3():
    lst = [1] * 15
    return all(lst)


if __name__ == "__main__":
    print(
        timeit.timeit(
            "f()",
            "from __main__ import f",
            number=10,
        )
    )
    print(
        timeit.timeit(
            "f2()",
            "from __main__ import f2",
            number=10,
        )
    )
    print(
        timeit.timeit(
            "f3()",
            "from __main__ import f3",
            number=10,
        )
    )
