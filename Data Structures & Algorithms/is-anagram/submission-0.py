class Solution:
    # Using hash map (Dictionary)
    def isAnagram(self, s: str, t: str) -> bool:
        dict1 = {}
        dict2 = {}
        for num in s:
            dict1[num] = dict1.get(num, 0) + 1

        for num in t:
            dict2[num] = dict2.get(num, 0) + 1

        print(dict1)
        print(dict2)

        if dict1 == dict2:
            return True

        return False

