class Solution:
    # input: ["act","pots","tops","cat","stop","hat"]
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        dict1 = defaultdict(list)
        # to create: {act:[0,3], opst:[1,2,4], aht:[5]}
        for i, st in enumerate(strs): # strs = ["act","pots","tops","cat","stop","hat"]
            st = ''.join(sorted(st)) # ''.join converts ['a', 'c', 't' to "act"]
            if st not in dict1:
                dict1[st] = [i] # {act:[0]}
            else:
                dict1[st].append(i)
        
        answer = []
        for v in dict1.values():
            temp = []
            for vv in v:
                temp.append(strs[vv])
            
            answer.append(temp)

        return answer    
        
        

        # convert {act:[0,3], pots:[1,2,4], hat:[5]} to [["hat"],["act", "cat"],["stop", "pots", "tops"]]
