class Solution {
    public int searchInsert(int[] nums, int target) {
        int l=0, r=nums.length-1;
        
        while(l<r){
            int middle = (l+r)/2;
            
            if(nums[middle] > target){
                r = middle-1;
            }else if (nums[middle] < target){
                l = middle+1; 
            }else{
                return middle;
            }
        }
        
        System.out.println("l & r =" + l + r);
        
        return l;
    }
}