class Solution {
    public int removeDuplicates(int[] nums) {
        int writer = 0, count = 1;
        for(int reader = 0; reader < nums.length; reader++){
            if(nums[reader] == nums[writer]){
                count += 1;
            } else{
                count = 1;
            }

            if(count <= 2){
                writer += 1;
                nums[writer] = nums[reader];
            }
        }

        return writer + 1;
    }
}