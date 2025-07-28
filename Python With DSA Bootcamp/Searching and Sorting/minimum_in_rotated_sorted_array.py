"""
Description:
Given a sorted array that has been rotated, find the minimum element in the array. The array was originally sorted in ascending order and then rotated at some pivot.


Parameters:

nums (List[int]): A list of integers sorted in ascending order but rotated at an unknown pivot.

Return Values:

int: The minimum element in the rotated sorted array.


Example:

Input: nums = [4, 5, 6, 7, 0, 1, 2] 
Output: 0 
Explanation: The minimum element is 0.
 
Input: nums = [11, 13, 15, 17] 
Output: 11 
Explanation: The array was not rotated, and the minimum element is the first element.
"""

def findMin(nums):
    size = len(nums)
    
    low = 0
    high = size - 1
    
    while (low <= high): 
        mid = (low+high)//2
        if (nums[mid] < nums[mid+1] and nums[mid] < nums[mid-1]):
            return nums[mid]
        elif nums[mid] < nums[mid+1] and nums[mid] > nums[mid-1]:
            high = mid - 1
        else:
            low = mid + 1
    return nums[0]

print(findMin([18, 10, 11, 13, 15, 17]))