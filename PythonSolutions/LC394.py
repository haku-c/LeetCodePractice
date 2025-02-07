from collections import deque


class Solution:
    def decodeString(self, s: str) -> str:
        queue = deque()
        for c in s:
            if c == "]":
                string = ""
                # groups the non-digit characters until we reach an open bracket.
                while queue:
                    current = queue.pop()
                    if current == "[":
                        # repeat based on the number
                        number = queue.pop()
                        queue.append(string * int(number))
                        break
                    else:
                        string = current + string
            # combine the numbers if there are more than one digit
            elif queue and c.isdigit() and queue[-1].isdigit():
                num = queue.pop() + c
                queue.append(num)
            else:
                queue.append(c)

        return "".join(list(queue))
