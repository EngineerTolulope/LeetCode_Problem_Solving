class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        sign = '-' if numerator * denominator < 0 else ''
        numerator, denominator = abs(numerator), abs(denominator)
        
        quotient, remainder = divmod(numerator, denominator)
        result = [sign, str(quotient), '.']
        remainders = []
        
        while remainder not in remainders:
            remainders.append(remainder)
            quotient, remainder = divmod(remainder * 10, denominator)
            result.append(str(quotient))
        i = remainders.index(remainder) + 3
        result.insert(i, '(')
        result.append(')')
        result = ''.join(result).replace('(0)', '').rstrip('.')
        return result
        
        