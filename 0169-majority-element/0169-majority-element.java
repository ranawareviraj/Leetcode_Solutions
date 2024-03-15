class Solution {
    public int majorityElement(int[] nums) {
        int majorityElement = nums[0], count = 1;

        for (int i = 1; i < nums.length; i++) {
            if(count == 0)
                majorityElement = nums[i];
            
            count = majorityElement == nums[i] ? count + 1 : count - 1;

        }

        return majorityElement;
    }
}