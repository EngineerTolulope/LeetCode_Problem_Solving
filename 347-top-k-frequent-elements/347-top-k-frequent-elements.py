class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} # The Hash stores the count of elements
        top_nums = []   # Stores the result
        
        # It creates a bucket for every count frequency
        buckets = [[] for i in range(len(nums) + 1)]
        
        # Counts the numbers 
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        # The num is the key, and the count is the value
        for num, c in count.items():  
            buckets[c].append(num)   # This stores num at it's frequency index
            
        # The bucket now has the nums in their count index
        for bucket in buckets[::-1]:    # Starts the loop in reverse order
            for num in bucket:  # One bucket can have multiple numbers
                top_nums.append(num)
                if len(top_nums) == k:
                    return top_nums
            
        
        
        
            
        