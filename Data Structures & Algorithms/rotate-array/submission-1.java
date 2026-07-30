 
class Solution {
    public void rotate(int[] nums, int k) {
        k = k%nums.length;
        int n = nums.length;
        int[] second = Arrays.copyOfRange(nums, 0, n-k);
        int[] first = Arrays.copyOfRange(nums, n-k, n);
        
        for(int i=0;i<first.length;i++){
            nums[i] = first[i];
        }
        for(int i=0;i<second.length;i++){
            nums[i+first.length] = second[i];
        }
        
    }
}