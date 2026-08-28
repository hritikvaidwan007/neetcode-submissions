class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict1 = defaultdict(list) # means value of each key is list type [] by default

        for st in strs: # ["act","pots","tops","cat","stop","hat"]

            # Step 1: Create frequency array for provided string
            freq_arr = [0] * 26
            for ch in st: # ['a', 'c', 't']
                freq_arr[ord(ch) - ord('a')] += 1 # ord calculates ascii value
            # freq_arr = [1,2,0,3,1,2,.....2,1]

            # Step 2: Create dict {freq_arr: st}
            dict1[tuple(freq_arr)].append(st) # Hint: tuple used because key cannot be a list. key can be a tuple.
            # dict1 = {(0,2,1,2,3....,0,3,1): ["act", "cat"], (0,1,1,3,2....,1,1,0): ["stop", "post", "tops"]}

        # extract answer from dict1 
        return list(dict1.values())
        

        