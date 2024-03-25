class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left, result = 0, 0
        window_count = {}

        for right in range(len(fruits)):
            fruit = fruits[right]
            window_count[fruit] = 1 + window_count.get(fruit, 0)
            
            while len(window_count) > 2:
                left_fruit = fruits[left]
                window_count[left_fruit] -= 1
                left += 1

                if not window_count[left_fruit]:
                    window_count.pop(left_fruit)
            
            window_length = right - left + 1
            result = max(result, window_length)

        return result

            