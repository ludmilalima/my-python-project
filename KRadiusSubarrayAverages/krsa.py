class Solution(object):
    def getAverages(self, nums, k):
        result = [-1] * len(nums)
        window_size = 2 * k + 1

        if len(nums) < window_size:
            return result
        
        accumulate = sum(nums[:window_size])
        result[k] = accumulate // window_size

        for item in range(window_size, len(nums)):
            accumulate += nums[item] - nums[item - window_size]
            result[item - k] = accumulate // window_size
        return result

def main():
    with open("/workspaces/my-python-project/KRadiusSubarrayAverages/input.txt", "r") as file:
        line = file.readlines().pop()

    nums = list(map(int, line.replace('[','').replace(']','').split(',')))
    k = int(100000)
    solution = Solution()
    result = solution.getAverages(nums, k)
    for item in range(0, len(result)):
        print(f"{result[item]} ")

if __name__ == "__main__":
    main()