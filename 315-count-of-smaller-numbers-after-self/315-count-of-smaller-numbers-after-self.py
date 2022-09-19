from sortedcontainers import SortedList

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        
        nums = nums[::-1]
        sorted_list = SortedList()
        sorted_list.add(nums[0])
        result = [0]
        
        for i in range(1, len(nums)):
            num = nums[i]
            small_count = SortedList.bisect_left(sorted_list, num)
            result.append(small_count)
            sorted_list.add(num)
        return result[::-1]
        
        
            