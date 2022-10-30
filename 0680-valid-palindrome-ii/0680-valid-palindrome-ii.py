class Solution:
    def validPalindrome(self, s: str) -> bool:
        def valid_normal_palindrome(left, right):
            while left <= right:
                if s[left] == s[right]:
                    left += 1
                    right -= 1
                else:
                    return False
            return True
        
        
        left, right = 0, len(s) - 1
        while left <= right:
            if s[left] != s[right]:
                skip_left = valid_normal_palindrome(left + 1, right)
                skip_right = valid_normal_palindrome(left, right - 1)
                return skip_left or skip_right
            else:
                left += 1
                right -= 1
        return True
                