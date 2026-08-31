class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        // nums = nums = [5, 2, 5, 8, 2, 5, 8, 3, 2], k = 2

        // Step 1: Create frequency map of each number (key = number, value = frequency)
        // Dict:
        // 5 → 3
        // 2 → 3
        // 8 → 2
        // 3 → 1
        HashMap<Integer, Integer> freqMap = new HashMap<>();
        for (int num : nums) {
            freqMap.put(num, (freqMap.getOrDefault(num, 0) + 1));
        }

        // Step 2: Min heap based on frequency
        // min heap: smaller elements on top, bigger on bottom
        // A min-heap poll operation removes elements from above

        // By default, Java's PriorityQueue is a Min Heap. i.e PriorityQueue<Integer> heap = new PriorityQueue<>();
        // means if you add 5 -> 2 -> 8 -> 1 -> 6, then heap.poll() returns 1 (becaise 1 is smallest)

        // Inserting into heap (Heapify): O(n) 
        // popping from heap k times: k x log(n) ~ nlogn

        // PriorityQueue<Integer> : heap contains integers

        // PriorityQueue<int[]>   : heap contains int[] arrays (each element of heap is now an array)
        // Eg: you can add:
        // heap1.offer(new int[]{5, 3});
        // heap1.offer(new int[]{2, 3});
        // heap1.offer(new int[]{8, 2});

        // (a, b) -> a[0] - b[0] : it is a lambda expression.
        // It helps java to decide : When I have two arrays, which one should have higher priority?"
        // a = first array , b = second array
        // a = [8, 2],     b = [2, 3]
        // then a[0] is 8,    b[0] is 2
        // a[0] - b[0] = 8 - 2 = 6
        PriorityQueue<Integer> minHeap = new PriorityQueue<>((a, b) -> freqMap.get(a) - freqMap.get(b));

        // Step 3: Keep only k most frequent elements
        for(int num : freqMap.keySet()) {
            minHeap.offer(num);

            if (minHeap.size() > k) {
                minHeap.poll();
            }
        }

        // Step 4: Put heap elements into result
        int[] answer = new int[k];

        for(int i = 0; i < k; i++) {
            answer[i] = minHeap.poll();
        }

        return answer;
        // answer: [5,2]

    }
}