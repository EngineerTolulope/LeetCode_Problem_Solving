# class Solution:
#     def maximumRemovals(self, s, p, removable):
#         left = 0
#         right = len(removable) - 1
#         result = 0

#         while left <= right:
#             mid = (left + right) // 2
#             if self.isSubsequence(s, p, removable, mid + 1):
#                 result = mid + 1
#                 left = mid + 1
#             else:
#                 right = mid - 1

#         return result

#     def isSubsequence(self, s, p, removable, k):
#         chars = list(s)

#         for i in range(k):
#             chars[removable[i]] = '*'

#         pIndex = 0
#         for c in chars:
#             if c == p[pIndex]:
#                 pIndex += 1
#                 if pIndex == len(p):
#                     return True  # p is a subsequence of s

#         return False  # p is not a subsequence of s


class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        def is_subsequence(long_string, subsequence, removed):
            j = 0

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