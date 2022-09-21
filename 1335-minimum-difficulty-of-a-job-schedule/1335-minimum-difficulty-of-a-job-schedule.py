class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        @lru_cache(None)
        def dp(index, remain_days):
            if remain_days == 0:
                if index == job_length:
                    return 0
                else:
                    return sys.maxsize
            
            if index == job_length:
                if remain_days == 0:
                    return 0
                else:
                    return sys.maxsize
                
            result = sys.maxsize
            current_max = 0
            for i in range(index, job_length):
                current_max = max(current_max, jobDifficulty[i])
                result = min(result, current_max + dp(i+1, remain_days-1))
            return result
        
        job_length = len(jobDifficulty)
        if job_length < d:
            return -1
        
        return dp(0, d)