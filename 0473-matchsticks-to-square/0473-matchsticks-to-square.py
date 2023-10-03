class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        # Check for an empty matchsticks list
        if not matchsticks:
            return False

        total_length = sum(matchsticks)
        side_length = total_length // 4

        # Check if total length is divisible by 4
        if total_length % 4 != 0:
            return False

        # Create a list to track remaining length needed for each side
        target_sides = [side_length] * 4

        # Sort the matchsticks in descending order to optimize backtracking
        matchsticks.sort(reverse=True)

        def dfs(index):
            # Base case: all matchsticks have been used
            if index == len(matchsticks):
                return True

            # Try placing the current matchstick on each side of the square
            for i in range(4):
                if target_sides[i] >= matchsticks[index]:
                    target_sides[i] -= matchsticks[index]  # Update remaining length
                    if dfs(index + 1):  # Recursively check the next matchstick
                        return True
                    target_sides[i] += matchsticks[index]  # Backtrack by restoring the original state

            return False

        return dfs(0)

    # initial
    def makesquare_(self, matchsticks: List[int]) -> bool:
        square_lengths = {"up": 0, "down": 0, "left": 0, "right": 0}
        total_length = sum(matchsticks)
        side_length = total_length // 4

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