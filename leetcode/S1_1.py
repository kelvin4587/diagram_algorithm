from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i: int = 0
        j: int = 0
        while i < len(nums):
            j = i + 1
            while j < len(nums):
                if nums[i] + nums[j] == target:
                    return [i, j]
                j += 1
            i += 1
        return [0,0]


if __name__ == '__main__':
    s = Solution()
    print(s.twoSum([2, 7, 11, 15], 9))
    print(s.twoSum([3, 4, 2], 6))
    print(s.twoSum([3, 3], 6))
    print(s.twoSum([3, 3], 5))
