class Solution:
    # Using hash map (Dictionary)
    # with single loop
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        freq1 = [0] * 26
        freq2 = [0] * 26

        # you can also use 1 loop instead of 2 because both have same length
        for i,c in enumerate(s):
            freq1[ord(c)-ord('a')] += 1

        for i,c in enumerate(t):
            freq2[ord(c)-ord('a')] += 1

        if freq1 == freq2:
            return True
        else:
            return False
        