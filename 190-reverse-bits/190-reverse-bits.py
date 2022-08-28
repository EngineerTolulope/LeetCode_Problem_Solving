class Solution:
    def reverseBits(self, n: int) -> int:
        num = list("{:032b}".format(n))
        left, right = 0, len(num) - 1

        while left <= right:
            if num[left] == num[right]:
                left += 1
                right -= 1
                continue
            num[left], num[right] = num[right], num[left]
            left += 1
            right -= 1
        num = "".join(num)
        return int(num, 2)