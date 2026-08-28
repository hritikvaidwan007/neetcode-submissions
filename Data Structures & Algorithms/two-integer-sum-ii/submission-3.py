class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # numbers = [3,4,5,7,10,11]
        # target = 9
        # output = [2,3]
        # Hint: Take advantage of sorted array

        dict1 = {}
        i = 1
        for num in numbers:
            dict1[num] = i
            i = i + 1
        print(dict1)

        for num in dict1:
            if target - num in dict1:
                return [dict1[num], dict1[target - num]]

        else:
            return []
