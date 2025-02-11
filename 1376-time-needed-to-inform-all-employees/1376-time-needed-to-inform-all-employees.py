class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        adj = defaultdict(list) # ManagerID -> List of Employees
        for i in range(n):
            adj[manager[i]].append(i)
        
        result = 0
        queue = deque([(headID, 0)])

        while queue:
            managerID, time = queue.popleft()
            result = max(result, time)

            for empID in adj[managerID]:
                queue.append((empID, time + informTime[managerID]))
        
        return result