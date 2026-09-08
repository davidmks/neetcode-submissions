class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        result = float("inf")

        while left <= right:
            if nums[left] < nums[right]:
                return min(result, nums[left])
                break

            mid = (left + right) // 2
            result = min(result, nums[mid])
            
            if nums[left] <= nums[mid]:
                left = mid + 1
            else:
                right = mid - 1

        return result
