class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left, right, result = 0, len(people) - 1, 0
        while left <= right:
            remain = limit - people[right]
            right -= 1
            result += 1
            if left <= right and remain >= people[left]:
                left += 1
        return result