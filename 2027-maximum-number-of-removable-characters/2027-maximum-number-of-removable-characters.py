class Solution:
    def maximumRemovals(self, s, p, removable):
        left = 0
        right = len(removable)
        result = 0

        while left <= right:
            mid = left + (right - left) // 2
            if self.isSubsequence(s, p, removable, mid):
                result = mid
                left = mid + 1
            else:
                right = mid - 1

        return result

    def isSubsequence(self, s, p, removable, k):
        chars = list(s)

        for i in range(k):
            chars[removable[i]] = '*'

        pIndex = 0
        for c in chars:
            if c == p[pIndex]:
                pIndex += 1
                if pIndex == len(p):
                    return True  # p is a subsequence of s

        return False  # p is not a subsequence of s