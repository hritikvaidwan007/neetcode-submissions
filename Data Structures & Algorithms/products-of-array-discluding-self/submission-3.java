class Solution {
    public int[] productExceptSelf(int[] nums) {
        // Input: nums = [1,2,4,6]
        // Output: [48,24,12,8]

        // int[] arr = new int[5];
        // or int[] arr = {};
        // or int[] arr = new int[0];

        // output[i] = (product of everything LEFT of i) × (product of everything RIGHT of i)
        // index:       0    1    2    3
        // nums:       [1,   2,   4,   6]
        // left:       [1,   1,   2,   8]
        // right:      [48, 24,   6,   1]
        // answer:     [48,  24,  12,   8]
        
        int n = nums.length;

        int[] answer = new int[n];
        int[] left = new int[n];
        int[] right = new int[n];

        left[0] = 1;  
        right[n-1] = 1;

        // Creating left products
        // nums:       [1,   2,   4,   6]
        // left:       [1,   1,   2,   8]
        for(int i=1; i<n; i++) {
            left[i] = nums[i-1] * left[i-1];
        }

        // nums:       [1,   2,   4,   6]
        // right:      [48, 24,   6,   1]
        for(int i=n-2; i>=0; i--) {
            right[i] = nums[i+1] * right[i+1];
        }

        for(int i=0; i<n; i++) {
            answer[i] = left[i] * right[i];
        }

        return answer;

    }
}  
