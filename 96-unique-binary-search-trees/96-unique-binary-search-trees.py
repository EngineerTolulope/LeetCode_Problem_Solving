class Solution:
    def numTrees(self, n: int) -> int:
        num_tree = [1] * (n + 1)
        for node_count in range(2, n + 1):
            total = 0
            for root in range(1, node_count + 1):
                left = root - 1
                right = node_count - root
                total += num_tree[left] * num_tree[right]
            num_tree[node_count] = total
        return num_tree[n]