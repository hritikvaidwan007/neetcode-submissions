class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p_product = [] # prefix product (left to right)
        s_product = [] # suffix product (right to left)

        # nums = [2, 3, 1, 1, 4]

        temp = 1
        for num in nums:
            temp = temp * num
            p_product.append(temp)
        
        temp = 1
        for num in nums[::-1]: # or use: reversed(nums)
            temp = temp * num
            s_product.append(temp)
        s_product.reverse()

        # print("Input     :", nums)
        # print("p_product :",p_product)
        # print("s_product :",s_product)
        # print("Output    :",[12,8,24,24,6])

        answer = []
        answer.append(s_product[1])

        for i in range(1, len(nums)-1):
            answer.append(p_product[i-1] * s_product[i+1])

        answer.append(p_product[-2])

        return answer
        
