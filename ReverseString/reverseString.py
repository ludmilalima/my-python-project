
from typing import List

class Solution:
    def reverseStringSlice(self, s: List[str]) -> None:
        s[:] = s[::-1]

    def reverseStringWhile(self, s: List[str]) -> None:
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

    def reverseStringRecursion(self, s: List[str]) -> None:
        def helper(left: int, right: int) -> None:
            if left >= right:
                return
            s[left], s[right] = s[right], s[left]
            helper(left + 1, right - 1)

        helper(0, len(s) - 1)

    def reverseDoWhile(self, s: List[str]) -> None:
        left, right = 0, len(s) - 1
        while True:
            if left >= right:
                break
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

    def reverseStringFor(self, s: List[str]) -> None:
        n = len(s)
        for i in range(n // 2):
            s[i], s[n - 1 - i] = s[n - 1 - i], s[i]

    def reverseStringXorSwap(self, s: List[str]) -> None:
        n = len(s)
        for i in range(len(s) // 2):
            s[i] = chr(ord(s[i]) ^ ord(s[n - 1 - i]))
            s[n - 1 - i] = chr(ord(s[i]) ^ ord(s[n - 1 - i]))
            s[i] = chr(ord(s[i]) ^ ord(s[n - 1 - i]))
    

def main():
    solution = Solution()
    s = ["H", "e", "l", "l", "o", " ", "W", "o", "r", "l", "d", "!", "!", "!", "!", "!"]
    solution.reverseString(s)
    print(s)

if __name__ == "__main__":
    main()