from sortedcontainers import SortedList
class Solution(object):
    def getSkyline(self, buildings):
        events = []
        for l, r, h in buildings:
            events.append((l, h, 0))
            events.append((r, h, 1))
            
        ans = []
        heights = SortedList([0])
            
        events.sort()
        n = len(events)
        i = 0
        while i < n:
            cur_x = events[i][0]
            
            while i < n and events[i][0] == cur_x:
                x, h, t = events[i]
                if t == 0:
                    heights.add(h)
                else:
                    heights.remove(h)
                
                i += 1
                
            if not ans or ans[-1][1] != heights[-1]:
                ans.append((x, heights[-1]))
        
        return ans