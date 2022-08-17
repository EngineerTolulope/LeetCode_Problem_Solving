class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        num_of_jobs = len(startTime)
        jobs = sorted(zip(startTime, endTime, profit), key=lambda x:x[1])
        end_times = [end for start, end, profit in jobs]
        
        dp = [0] * num_of_jobs
        dp[0] = jobs[0][2]  # profit of first job
        for i in range(1, num_of_jobs):
            start_time, end_time, profit = jobs[i]
            
            # not scheduling current job
            dp[i] = dp[i-1]
            
            # schedule current job
            index = bisect.bisect(end_times, start_time) - 1
            dp[i] = max(dp[i], (dp[index] if index >= 0 else 0) + profit)
            
        return dp[-1]