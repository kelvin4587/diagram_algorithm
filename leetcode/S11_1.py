from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        i: int = 0
        j: int = len(height) - 1
        area: int = 0
        while i < j:
            if height[i] < height[j]:
                i += 1
            elif height[j] < height[i]:
                j -= 1
            area = max(min(height[i], height[j]) * (j - i), area)
        return area


if __name__ == '__main__':
    s = Solution()
    #print(s.maxArea([2, 7, 11, 15]))
    print(s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))