class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Input: [-1, 0, 1, 2, -1, -4]
        nums.sort() # [-4, -1, -1, 0, 1, 2]
        # (-1, -1, 2) = 0,  (-1, 0, 1) = 0
        answer = []
        len1 = len(nums) # len1 = 6
        for i in range(len1): # range(6) # i = [0, 1, 2, 3, 4, 5]

            # Edge case 1: If number is a +ve numer, the ahead numbers can never sum to make 0
            if nums[i] > 0:
                break
            
            # Edge case 2: This blocks avoid duplicate triplet 
            # coz [-4, -1, -1, 0, 1, 2] creates 2 same triplets at i = 1 (i.e. -1) and at i = 2 (i.e. -1)
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            print(f"i = {i}")
            print("l,r")
            print("....")
            # this is a 2 SUM problem
            # Now use same 2 pointers approach just like last question:
            # nums[i] is target here
            l = i + 1 # l = 1
            r = len1-1  # r = 6-1 = 5

            while l < r:
                print (l,r)

                threesum = nums[i] + nums[l] + nums[r]

                if threesum < 0:
                    l += 1
                elif threesum > 0:
                    r -= 1
                else: # threesum == 0: 
                    answer.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l-1] and l < r: # just like line 16, it avoid output [[0,0,0], [0,0,0] for input nums=[0,0,0,0] 
                        l += 1

                
            print()

        return answer