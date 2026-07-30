class Solution {
    public int minSubArrayLen(int target, int[] nums) {
        int l=0, r=0;
        int currentSum = 0;
        int output = 0;
        
        while(l<=r && r<nums.length){
            currentSum += r;
            if (currentSum < target){
                r++;
            }else{
                output = Math.min(output,r-l+1);
                currentSum -= nums[l];
                l++;
            }
        }
        
        return output;
    }
}