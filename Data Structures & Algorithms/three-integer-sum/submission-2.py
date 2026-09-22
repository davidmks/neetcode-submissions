class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        triplets = []

        for i in range(n - 2):
            anchor = nums[i]

            if anchor > 0:
                break

            if i > 0 and anchor == nums[i - 1]:
                continue

            left, right = i + 1, n - 1
            while left < right:
                total = anchor + nums[left] + nums[right]
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    triplets.append([anchor, nums[left], nums[right]])
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

        return triplets