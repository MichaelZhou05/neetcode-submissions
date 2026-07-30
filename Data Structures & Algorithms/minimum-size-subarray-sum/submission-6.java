class Solution {
    public int minSubArrayLen(int target, int[] nums) {
        int l=0, r=0;
        int currentSum = 0;
        int output = nums.length;
        
        while(l<=r && r<nums.length){
            System.out.println(currentSum);
            System.out.println("ptr" + l + r);
            
            if (currentSum < target){
                currentSum += nums[r];
                r++;
            }else{
                output = Math.min(output,r-l);
                currentSum -= nums[l];
                l++;
            }
        }
        while (currentSum > target){
            System.out.println(currentSum);
            output = Math.min(output,r-l);
            currentSum -= nums[l];
            l++;
        }
        
        output = Math.min(output,r-l);
        return output == nums.length ? 0:output;
    }
}