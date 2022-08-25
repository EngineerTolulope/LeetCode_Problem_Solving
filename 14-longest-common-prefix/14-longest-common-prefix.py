class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest_prefix, first_string = '', strs[0] 
        for i in range(len(first_string)):
            for string in strs:
                if i == len(string) or string[i] != first_string[i]:
                    return longest_prefix
            longest_prefix += first_string[i]
        return longest_prefix