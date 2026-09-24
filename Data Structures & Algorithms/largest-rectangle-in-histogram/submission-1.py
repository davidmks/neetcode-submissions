class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        
        for i, h in enumerate(heights):
            start = i
            while stack and h < stack[-1][1]:
                index, height = stack.pop()
                width = i - index
                max_area = max(max_area, width * height)
                start = index
            stack.append((start, h))
        
        while stack:
            index, height = stack.pop()
            width = len(heights) - index
            max_area = max(max_area, width * height)
        
        return max_area
