class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a, b = a[::-1], b[::-1]
        result, carry = "", 0
        
        for i in range(max(len(a), len(b))):
            num_a = int(a[i]) if i < len(a) else 0
            num_b = int(b[i]) if i < len(b) else 0
            total = num_a + num_b + carry
            result = str(total % 2) + result
            carry = total // 2
        
        return "1" + result if carry == 1 else result
            