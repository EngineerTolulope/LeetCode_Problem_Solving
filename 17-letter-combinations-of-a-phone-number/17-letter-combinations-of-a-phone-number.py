class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letter_combos = []  # List to store all letter combinations
        
        # Hash map to store characters each number maps to.
        num_to_char = { 
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', 
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }
        
        # Recursive function that gets all letter combinations
        def backtrack(i, curr_str):
            # Base case. If the current string matches our length of digits
            if len(curr_str) == len(digits):
                letter_combos.append(curr_str)
                return
            
            # Goes through each character for the digit at index i
            for char in num_to_char[digits[i]]:
                backtrack(i + 1, curr_str + char)
        # End of Helper Function
        
        # If it is not an empty string
        if digits:
            backtrack(0, "")    # Calls the recursive function starting at index 0
        
        return letter_combos
        
        
        
            
            
            
        