/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public int rob(TreeNode root) {

        int [] ret = dfs(root);
        return Math.max(ret[0],ret[1]);
        
    }


    public int[] dfs(TreeNode current){
        if(current == null){
            return new int[] {0,0};  //[lastnode included, NOTinlucded]
        }

        int[] left = dfs(current.left);
        int[] right = dfs(current.right);

        int include = current.val + left[1] + right[1];
        int notInclude = Math.max(left[1],left[0]) + Math.max(right[1],right[0]);

        return new int[] {include,notInclude};
        
    }
}