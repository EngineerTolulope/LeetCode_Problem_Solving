class Solution:
    def maxProduct(self, s: str) -> int:
        N, pali_map = len(s), {}
        
        for mask in range(1, 1 << N): # 1 << N == 2 ** N
            subseq = ''
            for i in range(N):
                if mask & (1 << i):
                    subseq += s[i]
            if subseq == subseq[::-1]:
                pali_map[mask] = len(subseq)
        
        result = 0
        for mask1 in pali_map:
            for mask2 in pali_map:
                if not (mask1 & mask2 == 0):
                    continue
                result = max(result, pali_map[mask1] * pali_map[mask2])
        return result