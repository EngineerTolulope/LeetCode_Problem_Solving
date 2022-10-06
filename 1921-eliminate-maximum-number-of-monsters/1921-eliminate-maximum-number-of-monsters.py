class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        arrival_time = []
        for x, spd in zip(dist, speed):
            time = math.ceil(x / spd)
            arrival_time.append(time)
        
        arrival_time.sort()
        result = 0
        for i in range(len(arrival_time)):
            if i >= arrival_time[i]:
                return result
            result += 1
        return result
            