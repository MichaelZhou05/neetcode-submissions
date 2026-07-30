class Solution {
    public int minSubArrayLen(int target, int[] nums) {
        int l=0, r=0;
        int currentSum = 0;
        int output = nums.length;
        
        while(l<=r && r<nums.length){
            if (currentSum < target){
             currentSum += r;
                r++;
            }else{
                output = Math.min(output,r-l+1);
                currentSum -= nums[l];
                l++;
            }
        }
        
        return output == nums.length ? 0:output;
    }
}