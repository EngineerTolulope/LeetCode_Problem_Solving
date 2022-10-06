class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        code_set = set()
        for i in range(len(s) - k + 1):
            sub_str = s[i:i+k]
            code_set.add(sub_str)
        return len(code_set) == 2**k