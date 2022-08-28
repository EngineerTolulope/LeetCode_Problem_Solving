class Solution:
    def reverseBits(self, n: int) -> int:
        num_list = list("{:032b}".format(n))
        left, right = 0, len(num_list) - 1

        while left <= right:
            if num_list[left] == num_list[right]:
                left += 1
                right -= 1
                continue
            num_list[left], num_list[right] = num_list[right], num_list[left]
            left += 1
            right -= 1
        num_string = "".join(num_list)
        return int(num_string, 2)