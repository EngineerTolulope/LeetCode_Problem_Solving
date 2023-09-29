from collections import deque

class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        queue = deque([0])
        farthest = 0
        s_length = len(s)
        ones = set()

        for i in range(s_length):
            if s[i] == "0":
                ones.add(i)

        while queue:
            index = queue.popleft()

            # Find the next valid position to jump to
            start = max(minJump + index, farthest + 1)
            end = min(maxJump + index, s_length - 1)

            for j in range(start, end + 1):
                if j in ones:
                    queue.append(j)

                    if j == s_length - 1:
                        return True

            # Update the farthest position reached
            farthest = max(farthest, end)

        return False