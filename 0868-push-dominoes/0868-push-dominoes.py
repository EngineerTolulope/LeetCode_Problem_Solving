class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        dominoes = list(dominoes)
        queue = deque()

        for index, domino in enumerate(dominoes):
            if domino != ".":
                queue.append((index, domino))
        
        while queue:
            index, domino = queue.popleft()
            if domino == "L":
                if index > 0 and dominoes[index - 1] == ".":
                    dominoes[index - 1] = "L"
                    queue.append((index - 1, "L"))
            elif domino == "R":
                if index + 1 < len(dominoes) and dominoes[index + 1] == ".":
                    if index + 2 < len(dominoes) and dominoes[index + 2] == "L":
                        queue.popleft()
                    else:
                        dominoes[index + 1] = "R"
                        queue.append((index + 1, "R"))
       
        return "".join(dominoes)