class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        result = 0
        previous = bank[0].count("1")

        for i in range(1, len(bank)):
            current = bank[i].count("1")
            if current:
                result += previous * current
                previous = current
        return result