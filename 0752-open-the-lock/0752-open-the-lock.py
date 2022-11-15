class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        def get_children(lock):
            result = []
            for i in range(4):
                digit = str((int(lock[i]) + 1) % 10)
                result.append(lock[:i] + digit + lock[i + 1:])
                
                digit = str((int(lock[i]) - 1) % 10)
                result.append(lock[:i] + digit + lock[i + 1:])
            return result
        
        visited = set(deadends)
        if '0000' in visited:
            return -1
        
        queue = deque()
        queue.append(('0000', 0))
        while queue:
            lock, turns = queue.popleft()
            if lock == target:
                return turns
            
            for child in get_children(lock):
                if child not in visited:
                    visited.add(child)
                    queue.append((child, turns + 1))
        return -1