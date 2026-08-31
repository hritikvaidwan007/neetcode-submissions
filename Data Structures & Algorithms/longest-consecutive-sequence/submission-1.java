class Solution {
    public int longestConsecutive(int[] nums) {
        // nums = [100, 4, 200, 1, 3, 2]
        // longest = [1, 2, 3, 4]
        // length = 4

        HashSet<Integer> set1 = new HashSet<>();

        for(int num : nums) {
            set1.add(num);
        }

        System.out.println(set1.toString());

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
