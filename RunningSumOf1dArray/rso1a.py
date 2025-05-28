from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        numsSize = len(nums)
        result: List[int] = []
        result.append(nums[0])
        for i in range(1, numsSize):
            result.append(result[i - 1] + nums[i])
        return result
    
if __name__ == "__main__":
    solution = Solution()
    nums = [1, 2, 3, 4]
    result = solution.runningSum(nums)
    print(result)