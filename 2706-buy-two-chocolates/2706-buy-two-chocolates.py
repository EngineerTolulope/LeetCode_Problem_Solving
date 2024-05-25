class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        min1 = min2 = sys.maxsize

        for price in prices:
            if price < min1:
                temp = min1
                min1 = price
                min2 = temp
            elif price < min2:
                min2 = price
                
        leftover = money - min1 - min2
        return leftover if leftover >= 0 else money