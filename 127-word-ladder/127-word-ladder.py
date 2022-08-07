class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        wordList.append(beginWord)
        neighbors = collections.defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + '*' + word[i+1:]
                neighbors[pattern].append(word)
        
        visited = set([beginWord])
        queue = collections.deque([beginWord])
        word_count = 1
        while queue:
            for _ in range(len(queue)):
                word = queue.popleft()
                if word == endWord:
                    return word_count
                for i in range(len(word)):
                    pattern = word[:i] + '*' + word[i+1:]
                    for neighbor in neighbors[pattern]:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            queue.append(neighbor)
            word_count += 1
        return 0
                    
        
