class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # 1. solution (two pointers)
        left, right = 0, len(arr) - 1
        while right - left + 1 > k:
            if x - arr[left] > arr[right] - x:
                left += 1
            else:
                right -= 1
        return arr[left : right + 1]

        # 2. solution (binary search)
        # TODO once I get to this chapter
