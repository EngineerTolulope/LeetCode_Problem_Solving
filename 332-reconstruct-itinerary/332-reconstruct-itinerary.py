class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort()
        
        adjacents = {source: [] for source, _ in tickets}
        for source, destination in tickets:
            adjacents[source].append(destination)
            
        result = ['JFK']
        def backtracking(source):
            if len(result) == len(tickets) + 1:
                return True
            if source not in adjacents:
                return False
            
            temp = adjacents[source].copy()
            for i, next_location in enumerate(temp):
                if next_location == '*': 
                    continue
                
                adjacents[source][i] = '*'
                result.append(next_location)
                if backtracking(next_location):
                    return True
                
                adjacents[source][i] = next_location
                result.pop()
            return False
        
        backtracking('JFK')
        return result
            