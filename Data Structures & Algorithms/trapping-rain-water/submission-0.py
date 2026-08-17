class Solution:
    def trap(self, height: List[int]) -> int:
        # 2. solution (two pointers)
        # Logic: you never use both maxes, only the smaller one. So you do not need to store them, just track a running max from each end and always work on the smaller side.
        left, right = 0, len(height) - 1
        left_max = right_max = 0
        total = 0

        while left < right:
            if height[left] < height[right]:
                # left wall is shorter - water it's limited to the left side
                left_max = max(left_max, height[left])
                total += left_max - height[left]
                left += 1
            else:
                right_max = max(right_max, height[right])
                total += right_max - height[right]
                right -= 1
        return total

        # # 1. solution (prefix - suffix)
        # n = len(height)
        # if n < 3:
        #     return 0
        # max_left = [0] * n
        # max_right = [0] * n

        # max_left[0] = height[0]
        # for i in range(1, n):
        #     max_left[i] = max(max_left[i - 1], height[i])

        # max_right[n - 1] = height[n - 1]
        # for i in reversed(range(n - 1)):
        #     max_right[i] = max(max_right[i + 1], height[i])

        # return sum(min(max_left[i], max_right[i]) - height[i] for i in range(n))
