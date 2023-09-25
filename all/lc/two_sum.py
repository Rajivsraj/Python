class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lst = []
        for x in range(len(nums)):
            for y in range(x+1, len(nums)):
                if nums[x]+nums[y] == target:
                    lst.append(x)
                    lst.append(y)

        return lst


nums = [2,7,11,15]
obj = Solution()
print(obj.twoSum(nums, 9))