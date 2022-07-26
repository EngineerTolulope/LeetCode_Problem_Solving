class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash_set = set()
        for num in nums:
            if num in hash_set: 
                return True
            else:
                hash_set.add(num)
        
        return False
    
    
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         new_arr = []
#         for num in nums:
#             if num in new_arr: 
#                 return True
#             else:
#                 new_arr.append(num)
        
#         return False

