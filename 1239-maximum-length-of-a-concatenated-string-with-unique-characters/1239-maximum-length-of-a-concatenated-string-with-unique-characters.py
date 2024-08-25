class Solution:
    def maxLength(self, arr: List[str]) -> int:
        charSet = set()

        def containsDuplicate(charSet, s):
            c = Counter(charSet) + Counter(s)
            return max(c.values()) > 1

        def backtrack(i):
            if i == len(arr):
                return len(charSet)

            result = 0
            if not containsDuplicate(charSet, arr[i]):
                for c in arr[i]:
                    charSet.add(c)
                result = backtrack(i + 1)
                for c in arr[i]:
                    charSet.remove(c)
            return max(result, backtrack(i + 1))

        return backtrack(0)