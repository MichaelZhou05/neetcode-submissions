
class Solution {
    public boolean hasDuplicate(int[] nums) {
        Set<Integer> set1 = new HashSet<>();
        for(int x :nums){
            set1.add(x);
        }

        return set1.size() != nums.length;
    }
}