class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total_elements = len(nums1) + len(nums2)
        half = total_elements // 2
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        left, right = 0, len(nums1) - 1
        while True:
            i = (left + right) // 2 # nums1
            j = half - i - 2    # nums2
            
            left_1 = nums1[i] if i >= 0 else float('-infinity')
            right_1 = nums1[i + 1] if (i + 1) < len(nums1) else float('+infinity')
            left_2 = nums2[j] if j >= 0 else float('-infinity')
            right_2 = nums2[j + 1] if (j + 1) < len(nums2) else float('+infinity')
            
            # partition is correct
            if left_1 <= right_2 and left_2 <= right_1:
                # odd
                if total_elements % 2 == 1:
                    return min(right_1, right_2)
                #even
                return (max(left_1, left_2) + min(right_1, right_2)) / 2
            elif left_1 > right_2:
                right = i - 1
            else:
                left = i + 1