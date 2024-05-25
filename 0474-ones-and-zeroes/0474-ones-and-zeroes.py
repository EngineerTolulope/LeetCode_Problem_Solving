class Solution:
    def findMaxForm(self, strs: List[str], M: int, N: int) -> int:
        dp = defaultdict(int)

        for s in strs:
            m_count, n_count = s.count("0"), s.count("1")
            for m in range(M, m_count - 1, -1):
                for n in range(N, n_count - 1, -1):
                    dp[(m, n)] = max(1 + dp[(m - m_count, n - n_count)], dp[(m, n)])
        return dp[(M, N)]