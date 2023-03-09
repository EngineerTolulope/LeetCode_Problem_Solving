class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_index = {num:i for i, num in enumerate(nums1)}
        mono_stack = []
        result = [-1] * len(nums1)
        
        for num in nums2:
            while mono_stack and num > mono_stack[-1]:
                prev_num = mono_stack.pop()
                index = nums1_index[prev_num]
                result[index] = num
            
            if num in nums1_index:
                mono_stack.append(num)
        return result