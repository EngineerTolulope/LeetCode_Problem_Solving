class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        sign = '-' if numerator*denominator < 0 else ''
        quotient, remainder = divmod(abs(numerator), abs(denominator))
#         print(quotient,remainder)
        result = [sign, str(quotient), '.']
        remainders = []
        while remainder not in remainders:
            remainders.append(remainder)
            quotient, remainder = divmod(remainder*10, abs(denominator))
#             print(quotient,remainder)
            result.append(str(quotient))
#         print(result)
#         print(remainders)
#         print(remainder)
        i = remainders.index(remainder)
#         print(i)
        result.insert(i+3,"(")
        result.append(")")
#         print(result)
        res = ''.join(result).replace('(0)',"").rstrip('.')
        return res