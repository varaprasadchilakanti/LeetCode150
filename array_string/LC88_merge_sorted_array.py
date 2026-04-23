"""
88. Merge Sorted Array
----------------------

Problem:
You are given two sorted integer arrays nums1 and nums2, and integers m and n representing
the number of valid elements in each. Merge nums2 into nums1 as one sorted array in-place.
nums1 has length m+n, with the last n slots reserved (set to 0).

Constraints:
- nums1.length == m + n
- nums2.length == n
- 0 <= m, n <= 200
- 1 <= m + n <= 200
- -10^9 <= nums1[i], nums2[j] <= 10^9
- Target complexity: O(m + n)

Strategy:
- Two-pointer technique from the end of both arrays.
- Fill nums1 backwards to avoid overwriting valid elements.
- Compare nums1[m-1] and nums2[n-1], place larger at nums1[m+n-1].
- Continue until nums2 is exhausted.

Edge Cases:
- nums2 empty → nums1 unchanged.
- nums1 empty (m=0) → nums1 replaced entirely by nums2.
- Duplicate values → naturally handled by comparison.

Design Notes:
- Encapsulated in a Solution class for consistency.
- Strategy abstraction for extensibility (e.g., alternative merge strategies).
- Explicit typing for clarity.
- Fail-fast: minimal branching beyond constraints.
"""

from typing import List, Protocol


class MergeStrategy(Protocol):
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None: ...


class TwoPointerMerge:
    """
    SRP: Encapsulates in-place merge logic using two-pointer technique.
    OCP: Can extend with other strategies (e.g., slice assignment, heap-based).
    """
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i, j, k = m - 1, n - 1, m + n - 1
        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1


class Solution:
    """
    High-level interface depending on abstraction (strategy).
    """
    def __init__(self, strategy: MergeStrategy = TwoPointerMerge()) -> None:
        self.strategy = strategy

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        self.strategy.merge(nums1, m, nums2, n)


if __name__ == "__main__":
    # Developer sanity tests
    nums1 = [1, 2, 3, 0, 0, 0]
    nums2 = [2, 5, 6]
    Solution().merge(nums1, 3, nums2, 3)
    print(nums1)  # Expected: [1, 2, 2, 3, 5, 6]

    nums1 = [1]
    nums2 = []
    Solution().merge(nums1, 1, nums2, 0)
    print(nums1)  # Expected: [1]

    nums1 = [0]
    nums2 = [1]
    Solution().merge(nums1, 0, nums2, 1)
    print(nums1)  # Expected: [1]
