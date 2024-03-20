from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        nums.sort()
        answer = []
        for first in range(0, length):
            if first == 0 or nums[first] != nums[first - 1]:
                third = length - 1
                for second in range(first + 1, length):
                    if second == first + 1 or nums[second] != nums[second - 1]:
                        while second < third and nums[first] + nums[second] + nums[third] > 0:
                            third = third - 1
                        if second == third:
                            break
                        if nums[first] + nums[second] + nums[third] == 0:
                            answer.append([nums[first], nums[second], nums[third]])
        return answer

if __name__ == '__main__':
    s = Solution()
    print(s.threeSum([-1,0,1,2,-1,-4]))