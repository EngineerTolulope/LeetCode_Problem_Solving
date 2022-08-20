class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        maxTask = max(Counter(tasks).values())
        maxRepeats = Counter(Counter(tasks).values())[maxTask]
        return max(len(tasks), maxTask * (1 + n) - n + maxRepeats - 1)