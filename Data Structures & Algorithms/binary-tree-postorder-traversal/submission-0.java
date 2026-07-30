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
    
    public List<Integer> postorderTraversal(TreeNode root) {
        List<Integer> ret = new ArrayList<Integer>();
        pso(root, ret);
        return ret;
    }

    public void pso(TreeNode root, List<Integer> output){
        if(root == null){
            return;
        }

        pso(root.left,output);
        pso(root.right,output);
        output.add(root.val);
        
    }   

}