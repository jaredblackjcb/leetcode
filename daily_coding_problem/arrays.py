# Return new arr where i = product of all elements except i
# [1,2,3] -> [6,3,2]
# Edge cases:
## [1] -> [0]
import math
from typing import List

# 1.1
def productOfAllOtherElements(arr: List[int]) -> List[int]:
    # Time: O(n)
    # Space: O(n)
    ans = []
    total = 1
    for x in arr:
        total *= x
    for x in arr:
        ans.append(total / x)
    return ans

# Without division using prefix and suffix products
def productOfAllOtherElements2(arr: List[int]) -> List[int]:
    # Time: O(n)
    # Space: O(n)
    # Get prefix products
    prefix = []
    for x in arr:
        if prefix:
            prefix.append(x * prefix[-1])
        else:
            prefix.append(x)

    # Get suffix products
    suffix = []
    for x in reversed(arr):
        if suffix:
            suffix.append(x * suffix[-1])
        else:
            suffix.append(x)
    # Don't forget to reverse the suffix list since it was computed in reverse order
    suffix.reverse()

    ans = []
    for i in range(len(arr)):
        if i == 0:
            ans.append(suffix[i+1])
        elif i == len(arr) - 1:
            ans.append(prefix[i-1])
        else:
            ans.append(prefix[i-1] * suffix[i+1])
    return ans

# 1.2
def smallestSortingWindow(arr:List[int]) -> tuple:
    # Time: O(n)
    # Space: O(1)
    left, right = 0, len(arr) - 1
    # Going left to right, if num < current max, add its index to the window as the right bound of the window
    maxSoFar = arr[0]
    for i, x in enumerate(arr):
        maxSoFar = max(maxSoFar, x)
        if x < maxSoFar:
            right = i

    # From right to left, if num > min, add to window
    minSoFar = arr[-1]
    for i, x in enumerate(reversed(arr)):
        minSoFar = min(minSoFar, x)
        if x > minSoFar:
            left = i

    return left, right

# 1.3
def maxContiguousSumBruteForce(arr: List[int]) -> int:
    # Time: O(n^3)
    currentMax = 0
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            currentMax = max(currentMax, sum(arr[i:j+1]))
    return currentMax

def maxContiguousSumKadanesAlgo(arr: List[int]) -> int:
    # Time: O(n)
    # Space: O(1)
    max_so_far = max_ending_here = 0
    for x in arr:
        max_ending_here = max(x, max_so_far + x)
        max_so_far = max(max_ending_here, max_so_far)
    return max_so_far

def minContiguousSum(arr: List[int]) -> int:
    min_so_far = min_ending_here = 0
    for x in arr:
        min_ending_here = min(x, min_ending_here + x)
        min_so_far = min(min_so_far, min_ending_here)
    return min_so_far

def maxContiguousWrapAroundSum(arr: List[int]) -> int:
    max_wrap_around = sum(arr) - minContiguousSum(arr)
    max_contiguous = maxContiguousSumKadanesAlgo(arr)
    return max(max_wrap_around, max_contiguous)


if __name__ == "__main__":
    print(maxContiguousWrapAroundSum([34,-50,42,14,-5,86]))