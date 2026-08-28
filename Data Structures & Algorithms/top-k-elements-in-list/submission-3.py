class Solution:
    # Using Min Heap 
    """
    After counting how often each number appears, we want to efficiently keep track of only the k most frequent elements.
    A min-heap is perfect for this because it always keeps the smallest element at the top.
    By pushing (frequency, value) pairs into the heap and removing the smallest whenever the heap grows beyond size k, we ensure that the heap always contains the top k most frequent elements.
    In the end, the heap holds exactly the k values with the highest frequencies.
    - heapq is min heap by default (where parent node is always smaller)
    - Heap has only to operations: heap push and heap pop. In min heap, heap push decides where to insert new node using hops, and in case of pop it always pops the root node. Nothing else.
    - remember heap is represented in Array (Youtube video)
    """
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict1 = {}
        for num in nums:
            dict1[num] = dict1.get(num,0) + 1
        # dict1 = {1: 1, 2: 2, 3: 3}

        heap1 = []
        for key in dict1:
            tuple1 = (dict1[key], key)
            heapq.heappush(heap1, tuple1)

            if len(heap1) > k:
                heapq.heappop(heap1)

        # heap1 = [(2,2), (3,3)]
        
        answer = []
        for tup in heap1:
            answer.append(tup[1])
        return answer

