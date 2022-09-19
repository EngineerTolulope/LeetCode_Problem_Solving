class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        previous, total_taxes = 0, 0
        for upper, percent in brackets:
            if income >= upper:
                total_taxes += (upper - previous) * percent / 100
                previous = upper
            else:
                total_taxes += (income - previous) * percent / 100
                return total_taxes
        return total_taxes