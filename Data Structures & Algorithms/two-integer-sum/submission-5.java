class Solution {
    public int[] twoSum(int[] nums, int target) {
        // new int[]{...} is used to create new int. eg -> new int[]{5, 10}
        
        // [3, 4, 5, 6, 5, 3], target = 7
        // then 7-3 = 4 (compliment) shoud exist in the array also
        // number and position array:
        // {
        //     3 : 0,
        //     4 : 1,
        //     4 : 2,
        //     6 : 3,
        //     5 : 4,
        //     3 : 5
        // }

        HashMap<Integer, Integer> map1 = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {

            int compliment = target - nums[i];
            if (map1.containsKey(compliment)) {
                return new int[]{map1.get(compliment), i};
            }

            map1.put(nums[i], i);
        }

        return new int[]{};
    }
}
