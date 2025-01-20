class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        n = len(derived)
        temp = [0] * n
        temp[0] = 0
        for i in range(1, n):
            if temp[i - 1] ^ 1 == derived[i - 1]:
                temp[i] = 1
            else:
                temp[i] = 0
        return (
            temp[-1] ^ temp[0] == derived[-1] or (~temp[-1]) ^ (~temp[0]) == derived[-1]
        )
