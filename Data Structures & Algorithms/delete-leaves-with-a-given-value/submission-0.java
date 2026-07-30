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


    1) postOrder Traverse Array
    2) set current Node's left and right child to be the return value of recurisve call
    3) call returns null if its leaf node && == target val
 */
class Solution {
    public TreeNode removeLeafNodes(TreeNode root, int target) {
        return postOrderTraversal(root,target);
    }

    public TreeNode postOrderTraversal(TreeNode current, int target){
        if(current == null){
            return null;
        }

        current.left = postOrderTraversal(current.left, target);
        current.right = postOrderTraversal(current.right, target);

        if(current.left == null && current.right == null && current.val == target){
            return null;
        }

        return current;


    }


    

}