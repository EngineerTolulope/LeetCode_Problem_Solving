class Solution:
    def dfs_filling(self, image, sr, sc, target_color, new_color):
        # Base Case
        if sr < 0 or sr >= len(image) or sc < 0 or sc >= len(image[0]) or image[sr][sc] != target_color:
            return
        
        image[sr][sc] = new_color
        self.dfs_filling(image, sr + 1, sc, target_color, new_color) # down
        self.dfs_filling(image, sr - 1, sc, target_color, new_color) # up
        self.dfs_filling(image, sr, sc - 1, target_color, new_color) # left
        self.dfs_filling(image, sr, sc + 1, target_color, new_color) # right
        
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image is None or image[sr][sc] == color:
            return image
        
        self.dfs_filling(image, sr, sc, image[sr][sc], color)
        return image
            
        
        
        