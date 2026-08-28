class Solution:
    # ord('A')
    # space complexity needed = 1 
    def isPalindrome(self, s: str) -> bool:

        def check_alpha(c):
            if (ord('A') <= ord(c) <= ord('Z')) or (ord('a') <= ord(c) <= ord('z')) or (ord('0') <= ord(c) <= ord('9')):
                return True
            else:
                return False
        
        
        i,j = 0, len(s) - 1

        while (i<j):
            # Part 1: Trim down special characters
            while (i < j) and check_alpha(s[i]) == False:
                i += 1
            while (j > i) and check_alpha(s[j]) == False:
                j -= 1

            # Part 2: Compare 2 pointers (also take lowercase)
            if s[i].lower()  !=  s[j].lower():
                print(f"comparing {s[i]} with {s[j]}")
                return False

            # to compare next pair
            i += 1
            j -= 1
                
        return True