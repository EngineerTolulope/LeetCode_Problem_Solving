class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        current_node = self.root
        
        for char in word:
            # If the current character is not a child of the current node
            if char not in current_node.children: 
                current_node.children[char] = TrieNode()    # Creates a new node if not a child
            current_node = current_node.children[char]  # Move to the child node
        
        current_node.end_of_word = True # Current node will be at the end of word node

        
    def search(self, word: str) -> bool:
        current_node = self.root
        
        for char in word:
            if char not in current_node.children:
                return False # Happens when there no node for the next word character
            current_node = current_node.children[char]
        
        return current_node.end_of_word # Returns true if we are at the end letter 
            
            
    def startsWith(self, prefix: str) -> bool:
        current_node = self.root
        
        for char in prefix:
            if char not in current_node.children:
                return False
            current_node = current_node.children[char]
        
        return True # We get here if we find a prefix, regardless if it is at the end of the word or not


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)