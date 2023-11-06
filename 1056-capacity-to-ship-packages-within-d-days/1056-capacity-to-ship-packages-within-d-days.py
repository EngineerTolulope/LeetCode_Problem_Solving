class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def is_capacity_okay(capacity):
            ships_count, current_capacity = 1, 0

            for weight in weights:
                if current_capacity + weight > capacity:
                    ships_count += 1
                    current_capacity = 0
                current_capacity += weight
            return ships_count <= days

        
        left, right = max(weights), sum(weights)
        result = right

        while left <= right:
            middle = (left + right) // 2
            if is_capacity_okay(middle):
                result = middle
                right = middle - 1
            else:
                left = middle + 1
        return result
            