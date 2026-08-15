class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # 1. solution (two pointers)
        left, right = 0, len(numbers) - 1 # O(1) space
        while left < right: # O(n) time
            total = numbers[left] + numbers[right]
            if total == target:
                return [left + 1, right + 1]
            if total > target:
                right -= 1
            else:
                left += 1
        return []
