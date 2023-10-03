class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        r_queue, d_queue = deque(), deque()

        for i, senator in enumerate(senate):
            if senator == "R":
                r_queue.append(i)
            else:
                d_queue.append(i)

        while d_queue and r_queue:
            d_senator = d_queue.popleft()
            r_senator = r_queue.popleft()
            
            if d_senator < r_senator:
                d_queue.append(d_senator + len(senate))
            else:
                r_queue.append(r_senator + len(senate))
        return "Radiant" if r_queue else "Dire"