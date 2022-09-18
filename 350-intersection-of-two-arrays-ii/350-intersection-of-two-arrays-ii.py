class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
            
        nums1_count = {}
        for num in nums1:
            nums1_count[num] = 1 + nums1_count.get(num, 0)
        
        i, result = 0, []
        while nums1_count and i < len(nums2):
            num = nums2[i]
            if num in nums1_count:
                result.append(num)
                nums1_count[num] -= 1
                if nums1_count[num] == 0:
                    nums1_count.pop(num)
            i += 1
        return result