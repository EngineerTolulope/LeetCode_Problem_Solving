class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = [str(digit) for digit in digits]
        digits = list(str(int(''.join(digits)) + 1))
        digits = [int(digit) for digit in digits]
        return digits