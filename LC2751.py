def survivedRobotsHealths(
    self, positions: List[int], healths: List[int], directions: str
) -> List[int]:
    positionsSorted = sorted(range(len(positions)), key=lambda k: positions[k])
    stack = []
    for i in range(len(positions)):
        current = positionsSorted[i]
        while len(stack) > 0 and healths[current] > 0:
            recent = stack[-1]
            # if the directions conflict
            if directions[recent] == "R" and directions[current] == "L":
                if healths[current] > healths[recent]:
                    rem = stack.pop()
                    healths[rem] = 0
                    healths[current] -= 1
                elif healths[current] == healths[recent]:
                    rem = stack.pop()
                    healths[rem] = 0
                    healths[current] = 0
                else:
                    healths[recent] -= 1
                    healths[current] = 0
            # if directions don't conflict
            else:
                stack.append(current)
                break
        if len(stack) == 0:
            stack.append(current)
    res = []
    for health in healths:
        if health > 0:
            res.append(health)
    return res

    # the following solution is more efficient because if there are consecutive lefts without a corresponding right bot,
    # there will never be a collision there. So it leverages when the stack is empty to avoid recomputation

    # def survivedRobotsHealths(
    #     self, positions: List[int], healths: List[int], directions: str
    # ) -> List[int]:
    #     n = len(positions)
    #     indices = list(range(n))
    #     result = []
    #     stack = []

    #     # Sort indices based on their positions
    #     indices.sort(key=lambda x: positions[x])

    #     for current_index in indices:
    #         # Add right-moving robots to the stack
    #         if directions[current_index] == "R":
    #             stack.append(current_index)
    #         else:
    #             while stack and healths[current_index] > 0:
    #                 # Pop the top robot from the stack for collision check
    #                 top_index = stack.pop()
    #                 print(top_index)
    #                 print(current_index)
    #                 print("---")
    #                 if healths[top_index] > healths[current_index]:
    #                     # Top robot survives, current robot is destroyed
    #                     healths[top_index] -= 1
    #                     healths[current_index] = 0
    #                     stack.append(top_index)
    #                 elif healths[top_index] < healths[current_index]:
    #                     # Current robot survives, top robot is destroyed
    #                     healths[current_index] -= 1
    #                     healths[top_index] = 0
    #                 else:
    #                     # Both robots are destroyed
    #                     healths[current_index] = 0
    #                     healths[top_index] = 0

    #     # Collect surviving robots
    #     for index in range(n):
    #         if healths[index] > 0:
    #             result.append(healths[index])

    #     return result
