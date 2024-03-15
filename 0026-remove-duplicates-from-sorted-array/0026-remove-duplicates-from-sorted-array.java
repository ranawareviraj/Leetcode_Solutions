class Solution {
    public int removeDuplicates(int[] nums) {
        int writer = 0;

        for (int reader = 0; reader < nums.length; reader++) {
            if (nums[writer] != nums[reader]) {
                writer += 1;
                nums[writer] = nums[reader];
            }
        }

        return writer + 1;
    }
}