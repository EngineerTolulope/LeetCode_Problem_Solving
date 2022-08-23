class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow_1, slow_2, fast = 0, 0, 0
        while True:
            slow_1 = nums[slow_1]
            fast = nums[nums[fast]]
            if slow_1 == fast:
                break

        while True:
            slow_1 = nums[slow_1]
            slow_2 = nums[slow_2]
            if slow_1 == slow_2:
                return slow_1
            
            
        