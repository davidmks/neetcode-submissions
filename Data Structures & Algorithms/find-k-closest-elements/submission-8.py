class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # # two pointers
        # left, right = 0, len(arr) - 1
        # while right - left + 1 > k:
        #     if abs(x - arr[left]) <= abs(arr[right] - x):
        #         right -= 1
        #     else:
        #         left += 1
        # return arr[left : right + 1]

        # bin search
        left, right = 0, len(arr) - k
        while left < right:
            mid = (left + right) // 2
            if x - arr[mid] <= arr[mid + k] - x:
                right = mid
            else:
                left = mid + 1
        return arr[left : left + k]
