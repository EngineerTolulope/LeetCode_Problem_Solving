class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False
        
    def add_word(self, word):
        current = self
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode() # Creates a new trie node
            current = current.children[char]    # Moves to the newly created or old trie node
        current.end_of_word = True  # At this point we are at the end of the word

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        # Add all new words to root of the trie
        root = TrieNode()
        for word in words:
            root.add_word(word)
            
        ROWS, COLUMNS = len(board), len(board[0])  # Gets the width and height of the board
        found, visited = set(), set()   # Variables to store the found words, and visited boxes
            
        def dfs_search(row, column, node, word):
            # Base Case
            if (row < 0 or column < 0 or row == ROWS or column == COLUMNS or # If out of bounds
                board[row][column] not in node.children or   # If not a valid neighbor 
                (row, column) in visited):
                return
            
            visited.add((row, column))  # Add it to the set we don't visit it again
            
            node = node.children[board[row][column]]    # We move to the neigboring nodes
            word += board[row][column]  # Increments the word we are building
            
            if node.end_of_word:
                found.add(word)
             
            # Perfoms dfs search on each of it's neighbors
            dfs_search(row + 1, column, node, word)
            dfs_search(row - 1, column, node, word)
            dfs_search(row, column + 1, node, word)
            dfs_search(row, column - 1, node, word)
            
            visited.remove((row, column))   # Removes it so it could be used by the next node as a possible route
        # Goes through every row and column
        for row in range(ROWS):
            for column in range(COLUMNS):
                dfs_search(row, column, root, "")
        
        return list(found)