class Solution:
    # [3, 4, 5, 6, 5, 3], target = 7
    # then 7-3 = 4 (compliment) shoud exist in the array also
    # try with enum also
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict1 = {} # key stores number in array, value stores it's index in array
        for i, key in enumerate(nums):
            comlimentary = target - key
            if comlimentary in dict1:
                return [dict1[comlimentary], i]

            dict1[nums[i]] = i

        return []