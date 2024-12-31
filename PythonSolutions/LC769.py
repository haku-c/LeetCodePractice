from collections import deque
import bisect


class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        chunksMarkers = deque()
        chunksMarkers.append((0, 0))
        for i in range(1, len(arr)):
            current = arr[i]
            if current < arr[i - 1]:
                chunkStart = 0
                ind = bisect.bisect_left(arr[0:i], current)
                while chunksMarkers and ind <= chunksMarkers[-1][1]:
                    chunkStart, _ = chunksMarkers.pop()
                chunksMarkers.append((chunkStart, i))
                arr[chunkStart : (i + 1)] = sorted(arr[chunkStart : (i + 1)])
            else:
                chunksMarkers.append((i, i))

        return len(chunksMarkers)


# pop removes from the right of the queue. append adds to the right of the queue.
# to peek the most recently added element, index into the -1th element (the rightmost)


# here's a better solution:
class Solution:
    def maxChunksToSorted(self, arr):
        n = len(arr)
        chunks = 0
        max_element = 0

        # Iterate over the array
        for i in range(n):
            # Update max_element
            max_element = max(max_element, arr[i])

            if max_element == i:
                # All values in range [0, i] belong to the prefix arr[0:i]; a chunk can be formed
                chunks += 1

        return chunks


# this solution is also better. Relies on the idea that you shrink the size of the stack if the current element is out of order.
# keeps the stack monotonic increasing
class Solution:
    def maxChunksToSorted(self, arr):
        n = len(arr)
        # Deque to store the maximum elements of each chunk
        stack = deque()

        for i in range(n):
            # Case 1: Current element is larger, starts a new chunk
            if not stack or arr[i] > stack[-1]:
                stack.append(arr[i])
            else:
                # Case 2: Merge chunks
                max_element = stack[-1]
                while stack and arr[i] < stack[-1]:
                    stack.pop()
                stack.append(max_element)

        return len(stack)
