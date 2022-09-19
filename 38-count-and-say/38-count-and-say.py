class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        
        previous = self.countAndSay(n - 1)
        count, result = 1, ''
        for i in range(len(previous)):
            if (i + 1) < len(previous) and previous[i] == previous[i + 1]:
                count += 1
            else:
                result += str(count) + previous[i]
                count = 1
        return result