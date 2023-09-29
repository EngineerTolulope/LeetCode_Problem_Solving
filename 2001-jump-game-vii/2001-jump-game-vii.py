class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        queue = deque([0])
        farthest = 0
        s_length = len(s)

        while queue:
            index = queue.popleft()
            start = max(minJump + index, farthest + 1)
            end = min(maxJump + index, s_length - 1)

            for j in range(start, end + 1):
                if s[j] == "0":
                    queue.append(j)
                    if j == s_length - 1:
                        return True

            farthest = end

        return False