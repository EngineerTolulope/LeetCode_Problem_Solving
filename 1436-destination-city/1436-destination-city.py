class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        # Create a set of all starting cities
        starting_cities = {start for start, _ in paths}

        # Iterate through each path
        for _, end in paths:
            # If the destination city is not a starting city, it's the destination city
            if end not in starting_cities:
                return end