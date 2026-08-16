class Solution:
    def maxArea(self, heights: List[int]) -> int:
        best = 0
        left, right = 0, len(heights) - 1
        while left < right:
            h_left, h_right = heights[left], heights[right]
            width = right - left
            level = min(h_left, h_right)
            area = width * level
            best = max(best, area)
            if h_left < h_right:
                left += 1
            else:
                right -= 1
        return best
