from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        i: int = 0
        j: int = len(height) - 1
        area: int = 0
        while i < j:
            area = max(min(height[i], height[j]) * (j - i), area)
            if height[i] < height[j]:
                i += 1
            elif height[j] < height[i]:
                j -= 1
            elif height[i] == height[j]:
                i += 1
        return area


if __name__ == '__main__':
    s = Solution()
    print(s.maxArea([1, 2]))
    #print(s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))