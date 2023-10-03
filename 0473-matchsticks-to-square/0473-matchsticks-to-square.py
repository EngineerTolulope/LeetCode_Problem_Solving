class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        square_lengths = {"up" : 0, "down" : 0, "left" : 0, "right" : 0}
        total_length = sum(matchsticks)
        side_length = total_length / 4

        if total_length % 4 != 0:
            return False

        matchsticks.sort(reverse=True)

        def backtracking(i):
            if i == len(matchsticks):
                return True

            for key in square_lengths:
                if square_lengths[key] + matchsticks[i] <= side_length:
                    square_lengths[key] += matchsticks[i]
                    if backtracking(i + 1):
                        return True
                    
                    square_lengths[key] -= matchsticks[i]
            return False
        return backtracking(0)
        