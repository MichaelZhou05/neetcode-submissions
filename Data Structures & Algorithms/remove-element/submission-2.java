class Solution {
    public int removeElement(int[] nums, int val) {
        int offset = 0;
        for(int i=0; i<nums.length; i++){
            int j = i;
            if(nums[i] == val){
                while(i+offset < nums.length && nums[i+offset] == val){
                    offset++;
                }
                
                if(i+offset < nums.length){
                    int temp = nums[i];
                    nums[i] = nums[i+offset];
                    nums[i+offset] = temp;
                }
            }
            
        }
        
        return nums.length-offset;
    }
}