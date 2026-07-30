class Solution {
    public int removeElement(int[] nums, int val) {
        int l=0, r=0;
        int k = nums.length;
        while(r<nums.length){
            System.out.println(Arrays.toString(nums));
            if(nums[l] == val){
                while(r<nums.length && nums[r]==val){
                    r++;
                    k--;
                }
                
                System.out.println(l);
                System.out.println(r);
                if(r<nums.length){
                int temp = nums[l];
                nums[l] = nums[r];
                nums[r] = temp;}
            }
            l++;
            r++;
        }
        
        return k;
    }
}