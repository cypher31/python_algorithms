from typing import List

# Find the target element and return the index of the element

def binarySearch(nums: List, target: int) -> int:
    # divide the problem into two smaller sub problems
    # divide larger array into two smaller, depending on where the target lies
    # assume the provided array is sorted

    L = 0
    R = len(nums) - 1

    if nums[0] == target: return 0
    if nums[len(nums) - 1] == target: return len(nums) - 1

    while L < R:
        mid = (L + R) // 2
        midValue = nums[mid]
        if midValue == target:
            return mid
        if midValue > target:
            R = mid - 1
        if midValue < target:
            L = mid + 1
    return "Not Found"

def binarySearchTest():
    nums = range(10)
    print(list(nums), end="\n\n")

    # check 1
    target = 2
    search = binarySearch(nums, target)
    solution = 2
    print("The solution should be:", solution)
    print("The method returned:", search, end="\n\n")
    
    # check 2
    target = 5
    search = binarySearch(nums, target)
    solution = 5
    print("The solution should be:", solution)
    print("The method returned:", search, end="\n\n")

    # check 3
    target = 0
    search = binarySearch(nums, target)
    solution = 0
    print("The solution should be:", solution)
    print("The method returned:", search, end="\n\n")

    # check 4
    target = 9
    search = binarySearch(nums, target)
    solution = 9
    print("The solution should be:", solution)
    print("The method returned:", search, end="\n\n")

    # check 5
    target = 11
    search = binarySearch(nums, target)
    solution = "Not Found"
    print("The solution should be:", solution)
    print("The method returned:", search, end="\n\n")

if __name__ == "__main__":
    binarySearchTest()
