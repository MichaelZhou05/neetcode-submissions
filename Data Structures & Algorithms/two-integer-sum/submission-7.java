class Solution {
    public int[] twoSum(int[] nums, int target) {
         Map<Integer, Integer> pastNums = new HashMap<>(); // value --> index
        
        for(int i=0;i<nums.length; i++){
            if (pastNums.containsKey(target-nums[i])){
                return  i < (pastNums.get(target-nums[i])) ? new int[] {i,pastNums.get(target-nums[i])} : new int[] {pastNums.get(target-nums[i]), i};
            }
            pastNums.put(nums[i],i);
        }
        
        return null;
    }
}
