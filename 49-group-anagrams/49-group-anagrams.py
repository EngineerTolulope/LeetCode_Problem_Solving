class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)
        
        for string in strs:
            # Created an index for every lowercase character - From a to z
            count = [0]*26  
            
            # Count the occurence of each char in the string
            for char in string: 
                # Tries to get an index based on the ASCII value
                count[ord(char) - ord("a")] += 1    
                
            # Lists cannot be used as keys to a hash because it's mutable.
            group[tuple(count)].append(string) 
        
        return group.values()
        