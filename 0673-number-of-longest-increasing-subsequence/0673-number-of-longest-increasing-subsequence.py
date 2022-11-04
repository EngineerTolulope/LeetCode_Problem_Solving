class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        dp = {} # key = index, value = (length of LIS, count)
        length_LIS, result = 0, 0 # length of LIS, count of LIS
        
        # i = start of subseqeuence
        for i in range(len(nums) - 1, -1, -1):
            max_len, max_count = 1, 1   # len, count of LIS starting from i
            
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    length, count = dp[j]
                    if length + 1 > max_len:
                        max_len, max_count = length + 1, count
                    elif length + 1 == max_len:
                        max_count += count
            
            if max_len > length_LIS:
                length_LIS, result = max_len, max_count
            elif max_len == length_LIS:
                result += max_count
            dp[i] = (max_len, max_count)
        
        return result
            