class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        # Ensure nums1 is the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        total_len = m + n
        half_len = (total_len + 1) // 2

        # Perform binary search on nums1 to find the correct partition
        imin, imax = 0, m
        while imin <= imax:
            i = (imin + imax) // 2
            j = half_len - i

            # Check if the partition is valid
            if i < m and nums2[j-1] > nums1[i]:
                # i is too small, increase it
                imin = i + 1
            elif i > 0 and nums1[i-1] > nums2[j]:
                # i is too big, decrease it
                imax = i - 1
            else:
                # Found the correct partition
                # Handle edge cases for finding the maximum element of the left side
                if i == 0:
                    max_of_left = nums2[j-1]
                elif j == 0:
                    max_of_left = nums1[i-1]
                else:
                    max_of_left = max(nums1[i-1], nums2[j-1])

                if total_len % 2 == 1:
                    # Total length is odd, median is the maximum element of the left side
                    return max_of_left

                # Handle edge cases for finding the minimum element of the right side
                if i == m:
                    min_of_right = nums2[j]
                elif j == n:
                    min_of_right = nums1[i]
                else:
                    min_of_right = min(nums1[i], nums2[j])

                # Total length is even, median is the average of the maximum element of the left side
                # and the minimum element of the right side
                return (max_of_left + min_of_right) / 2.0
