class Solution:
    def trap(self, height: List[int]) -> int:
        # 2. solution (two pointers)
        max_left, max_right = 0, 0
        left, right = 0, len(height) - 1
        output = 0
        while left < right:
            max_left = max(max_left, height[left])
            max_right = max(max_right, height[right])
            if max_left < max_right:
                output += max_left - height[left]
                left += 1
            else:
                output += max_right - height[right]
                right -= 1
        return output

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
