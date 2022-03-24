
# Leetcode Q 1
# Given an array of integers and a target, return indicies of the two numbers
# which sum to the target

# Assumptions
#   Exactly one solution
#   Cannot use the same element twice

# Progress
#   Methods come up with the correct solution when given test cases
#   but they still need to be modified to not use the same element twice

class Solution: 
    def twoSumQuadratic(self, nums: list[int], target: int) -> list[int]:
        # O(n^2); Two nested for loops going through n values 
        for i in range(len(nums)):
            for j in range(1, len(nums)):
                sum = nums[i] + nums[j]
                if sum == target:
                    return [i, j]

    def twoSumTwoPass(self, nums: list[int], target: int) -> list[int]:
        # O(n) + O(n); Two for loops in series (correct nomenclature?) -> O(2n) -> O(n)
        complementDict = {}
        for i in range(len(nums)):
            comp = target - nums[i]
            complementDict[comp] = i
        
        for i in range(len(nums)):
            key = nums[i]
            if key in complementDict:
                return [i, complementDict[key]]

    def twoSumOnePass(self, nums: list[int], target: int) -> list[int]:
        # O(n); One for loop with nested O(1) if statement
        complementDict = {}
        for i in range(len(nums)):
            comp = target - nums[i]
            complementDict[comp] = i
            key = nums[i]

            if key in complementDict:
                return [i, complementDict[key]]

    def testTwoSumQuadratic(self):
        nums = [1, 3, 2, 6, 9, 100] # Solution is true in this data set
        target = int(12)
        solution = self.twoSumQuadratic(nums, target)

        if solution == [1, 4]:
            print("twoSumQuadratic is correct", solution)
        else:
            print("twoSumQuadratic error, incorrect solution."), solution

    def testTwoSumTwoPass(self):
        nums = [1, 3, 2, 6, 9, 100] # Solution is true in this data set
        target = int(6)
        solution = self.twoSumTwoPass(nums, target)

        if solution == [3, 4]:
            print("twoSumTwoPass is correct", solution)
        else:
            if solution[0] == solution[1]:
                print('Edge case, algorithm selecting the same index twice to reach target.')
            else:
                print("twoSumTwoPass error, incorrect solution.", solution)

    def testTwoSumOnePass(self):
        nums = [1, 3, 2, 6, 9, 100] # Solution is true in this data set
        target = int(109)
        solution = self.twoSumTwoPass(nums, target)

        if solution == [4, 5]:
            print("twoSumOnePass is correct", solution)
        else:
            if solution[0] == solution[1]:
                print('Edge case, algorithm selecting the same index twice to reach target.')
            else:
                print("twoSumOnePass error, incorrect solution.", solution)

if __name__ == "__main__":
    solution = Solution()
    Solution.testTwoSumQuadratic(solution)
    Solution.testTwoSumTwoPass(solution)
    Solution.testTwoSumOnePass(solution)


