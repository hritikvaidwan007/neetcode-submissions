class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # watch
        # nums = [100, 4, 200, 1, 3, 2]
        # set1 = (100, 4, 200, 1, 3, 2)
        # longest = [1, 2, 3, 4]
        # length = 4
        
        longest = 0
        num_set = set(nums)
        
        for num in num_set:
            if (num-1) not in num_set: # if no left neighbour exists, then it is start of Sequence (it will be true for 100, 200, 1)
                length = 1

                while((num + length) in num_set):
                    length +=1

                if length > longest:
                    longest = length
        
        return longest

            