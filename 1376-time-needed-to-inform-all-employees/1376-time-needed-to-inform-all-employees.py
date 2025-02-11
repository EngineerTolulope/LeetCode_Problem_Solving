from collections import defaultdict, deque
from typing import List

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        # Step 1: Build an adjacency list (org chart)
        org_chart = defaultdict(list)
        for empID in range(n):
            org_chart[manager[empID]].append(empID)

        # Step 2: Perform BFS to calculate max inform time
        queue = deque([(headID, 0)])  # (Employee ID, Accumulated Inform Time)
        max_time = 0

        while queue:
            managerID, curr_time = queue.popleft()
            max_time = max(max_time, curr_time)

            for empID in org_chart[managerID]:
                queue.append((empID, curr_time + informTime[managerID]))

        return max_time
