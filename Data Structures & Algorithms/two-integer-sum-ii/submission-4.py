class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # numbers = [3,4,5,7,10,11]
        # target = 9
        # output = [2,3]
        # Hint: Take advantage of sorted array

        l = 0
        r = len(numbers)-1

        while l<r:
            sum1 = numbers[l] + numbers[r]

            if sum1 == target:
                return [l+1, r+1]

            if sum1 < target:
                l += 1
            elif sum1 > target:
                r -= 1