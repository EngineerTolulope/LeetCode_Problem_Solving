class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        result = []

        left, right = 0, len(products) - 1
        for i, char in enumerate(searchWord):
            while left <= right and (len(products[left]) <= i or products[left][i] != char):
                left += 1
            while left <= right and (len(products[right]) <= i or products[right][i] != char):
                right -= 1
            
            result.append(products[left : left + min(3, right - left + 1)])
        return result