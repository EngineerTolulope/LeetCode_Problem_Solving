class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        continue_ = True
        i = len(digits) - 1
        
        while continue_:
            if i >= 0:
                if digits[i] == 9:
                    digits[i] = 0
                else:
                    digits[i] += 1
                    continue_ = False
            else:
                digits = [1] + digits
                continue_ = False
            i -= 1
        return digits 
    
    
        # digits = [str(digit) for digit in digits]
        # digits = list(str(int(''.join(digits)) + 1))
        # digits = [int(digit) for digit in digits]
        # return digits