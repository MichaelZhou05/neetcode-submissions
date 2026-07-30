import java.until.*;
class Solution {
    public boolean hasDuplicate(int[] nums) {
        Set<Integer> set1 = new HashSet<>(Arrays.asList(nums));

        return set1.size() == nums.length;
    }
}