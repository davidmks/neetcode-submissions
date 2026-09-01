class Solution:
    def trap(self, height: List[int]) -> int:
        # 2. solution (two pointers)
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        total = 0

        while left < right:
            if left_max < right_max:
                left += 1
                left_max = max(left_max, height[left])
                total += left_max - height[left]
            else:
                right -= 1
                right_max = max(right_max, height[right])
                total += right_max - height[right]
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
