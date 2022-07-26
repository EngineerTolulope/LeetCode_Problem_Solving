class TrieNode:
    def __init__(self):
        self.children = {}   # Stores the children an hash
        self.isEnd = False   # Sets the initial nodes to false 

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()  # We start at the root node

    def addWord(self, word: str) -> None:
        node = self.root    
        for char in word:
            if char in node.children:   # Checks if the character is a key in the children hash
                node = node.children[char]  # Moves to the node
            else:
                node.children[char] = TrieNode()    # Creates a new node
                node = node.children[char]  # Moves to the created node
        node.isEnd = True  # At this point we are at the end of the word

    def search(self, word: str) -> bool:
        stack = [(self.root, word)] # Our stacks contain tuples of the root node and the rest of the word
        
        # Keep running the loop until stack is empty
        while stack:
            node, word = stack.pop()    # Last In, First Out. Stack will be empty eventually.
            
            if not word:    # Gets here after when the word is an ""
                if node.isEnd:   # If the current node is an end 
                    return True
                                
             # If the first letter of the remaining word is a child of the node
            elif word[0] in node.children:
                new_node = node.children[word[0]]   # We go to the child node of the character 
                stack.append((new_node, word[1:]))  # We add the child node and remaining letters to the stack
            
            # If the character is a dot. 
            elif word[0] == ".":
                # Takes the node of each child of the current node and appends it to the stack
                for new_node in node.children.values(): # Returns the TrieNodes 
                    stack.append((new_node, word[1:]))
        
        return False
                    
                    
            
            


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)