from typing import List

class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        def is_subsequence(long_string, subsequence, removed):
            i, j = 0, 0

            for i in range(len(long_string)):
                if i not in removed and long_string[i] == subsequence[j]:
                    j += 1
                    if j == len(subsequence):
                        break
            return j == len(subsequence)

        result = 0
        left, right = 0, len(removable) - 1

        while left <= right:
            middle = (left + right) // 2
            removed = set(removable[:middle + 1])

            if is_subsequence(s, p, removed):
                result = middle + 1
                left = middle + 1
            else:
                right = middle - 1

        return result