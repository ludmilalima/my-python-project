from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        curr = 0
        ans = 0
        flipped = 0

        for index, value in enumerate(nums):
            if value == 0:
                if flipped < k:
                    flipped +=1
                else:
                    while nums[left] != 0:
                        left +=1
                    left +=1
            curr = index - left + 1
            ans = max(ans, curr)
        return ans

if __name__ == "__main__":
    nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
    k = 2
    solution = Solution()
    result = solution.longestOnes(nums, k)
    print(f"Longest sequence with at most {k} flips: {result}")