class Solution {
    public int missingNumber(int[] nums) {
        int sum = 0;
        for (int val : nums){
            sum += val;
        }

        return (nums.length)*(nums.length+1)/2 - sum;
    }
}
