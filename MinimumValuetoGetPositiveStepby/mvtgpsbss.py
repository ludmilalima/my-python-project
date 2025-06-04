from typing import List

class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        numsSize = len(nums)
        startValue = 1
        result: List[int] = []
        result.append(nums[0])
        startValue = max(startValue, result[0] * (-1) + 1)
        for i in range(1, numsSize):
            result.append(result[i - 1] + nums[i])
            startValue = max(startValue, result[i] * (-1) + 1)
        return startValue

if __name__ == "__main__":
    nums = [-12]
    solution = Solution()
    print(f"Minimum Value to Get Positive Step by Step: {solution.minStartValue(nums)}")