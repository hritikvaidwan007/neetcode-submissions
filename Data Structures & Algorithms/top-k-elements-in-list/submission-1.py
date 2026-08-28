class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict1 = {}

        # Step 1: Frequency dict
        for num in nums:
            dict1[num] = dict1.get(num,0) + 1
        # {1:4, 3:3, 2:2}
        
        # Step 2: {number:frequency} dict to [frequency, number] array.
        list1 = []
        for key in dict1:
            list1.append([dict1[key], key])

        # Step 3: sort array
        list1.sort(reverse=True)
        # [[4, 1], [3, 3], [2, 2]]

        answer = []
        for i in range(k): # k = 0,1
            answer.append(list1[i][1])

        return answer

        

       