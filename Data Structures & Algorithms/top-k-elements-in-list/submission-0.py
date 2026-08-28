class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict1 = {}

        for num in nums:
            dict1[num] = dict1.get(num,0) + 1
        # {1:4, 3:3, 2:2}
        

        list1 = []
        for key in dict1:
            list1.append([dict1[key], key])

        list1.sort(reverse=True)
        # [[4, 1], [3, 3], [2, 2]]

        answer = []
        for i in range(k): # k = 0,1
            answer.append(list1[i][1])

        return answer

        

       