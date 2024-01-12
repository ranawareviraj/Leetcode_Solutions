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
    public int findTilt(TreeNode root) {
        return dfs(root).tilt;
    }

    private static Result dfs(TreeNode node) {
        if (node == null) return new Result(0, 0);

        Result leftResult = dfs(node.left);
        Result rightResult = dfs(node.right);

        int tilt = Math.abs(leftResult.sum - rightResult.sum) + leftResult.tilt + rightResult.tilt;
        int sum = node.val + leftResult.sum + rightResult.sum;

        return new Result(sum, tilt);
    }

    private static class Result {
        int sum;
        int tilt;

        Result(int sum, int tilt) {
            this.sum = sum;
            this.tilt = tilt;
        }
    }
}
