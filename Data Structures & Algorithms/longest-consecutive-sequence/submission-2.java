class Solution {
    public int longestConsecutive(int[] nums) {
        // nums = [100, 4, 200, 1, 3, 2]
        // longest = [1, 2, 3, 4]
        // length = 4

        // STEP 1:
        // Create Hashset: because for each number, next consiqutive number 
        // will be found inside hashset to save time.
        HashSet<Integer> set1 = new HashSet<>();
        for(int num : nums) {
            set1.add(num);
        }

        // STEP 2:
        // pick a number from set, found it consequtives found in set
        // also track length of number of consequtives found
        int longest = 0;
        for(int num : set1) {
            if(!set1.contains(num-1)) {
                int length = 1;

                while(set1.contains(num + length)) {
                    length++;
                }
                longest = Math.max(longest, length);
            }
        }

        return longest;
    }
}
