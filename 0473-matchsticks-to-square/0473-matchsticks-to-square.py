class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        if not matchsticks:
            return False

        total_length = sum(matchsticks)
        side_length = total_length // 4

        if total_length % 4 != 0:
            return False

        target_sides = [side_length] * 4
        matchsticks.sort(reverse=True)

        def dfs(index):
            if index == len(matchsticks):
                return True

            for i in range(4):
                if target_sides[i] >= matchsticks[index]:
                    target_sides[i] -= matchsticks[index]
                    if dfs(index + 1):
                        return True
                    target_sides[i] += matchsticks[index]

            return False

        return dfs(0)