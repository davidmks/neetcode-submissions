class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(A) + len(B)
        half = total // 2

        if len(A) > len(B):
            A, B = B, A

        left, right = 0, len(A)
        while left <= right:
            i = (left + right) // 2
            j = half - i

            a_left = A[i - 1] if i > 0 else float("-inf")
            a_right = A[i] if i < len(A) else float("inf")
            b_left = B[j - 1] if j > 0 else float("-inf")
            b_right = B[j] if j < len(B) else float("inf")

            if a_left <= b_right and a_right >= b_left:
                if total % 2 == 0:
                    # even
                    return (max(a_left, b_left) + min(b_right, a_right)) / 2
                # odd
                return min(a_right, b_right)
            if a_left > b_right:
                right = i - 1
            else:
                left = i + 1
