class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = []

        for i, anchor in enumerate(nums):
            if anchor > 0:
                break
            if i > 0 and anchor == nums[i - 1]:  # same anchor value twice
                continue

            left, right = i + 1, len(nums) - 1
            print(left, right)
            while left < right:
                total = anchor + nums[left] + nums[right]
                if total == 0:
                    triplets.append([anchor, nums[left], nums[right]])
                    left += 1
                    while (
                        left < right and nums[left] == nums[left - 1]
                    ):  # same left value twice, under same anchor
                        left += 1
                elif total > 0:
                    right -= 1
                else:
                    left += 1
        return triplets
