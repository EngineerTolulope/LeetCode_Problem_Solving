class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        result = []

        for spell in spells:
            minimum_index = len(potions)

            left, right = 0, len(potions) - 1
            while left <= right:
                middle = (left + right) // 2
                if spell * potions[middle] >= success:
                    minimum_index = middle
                    right = middle - 1
                else:
                    left = middle + 1
            result.append(len(potions) - minimum_index)
        
        return result