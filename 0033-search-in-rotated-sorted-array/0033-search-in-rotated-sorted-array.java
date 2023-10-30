class Solution {
    public int search(int[] nums, int target) {
        int left = 0, right = nums.length - 1;

        while(left <= right){
            int mid = left + (right - left) / 2;

            int num = (nums[mid] < nums[0] == target < nums[0]) 
                        ? nums[mid]
                        : target < nums[0] ? Integer.MIN_VALUE : Integer.MAX_VALUE;

            if(num == target){
                return mid;
            }

            if(num < target){
                left = mid + 1;
            } else if (num > target){
                right = mid - 1;
            } 
        }

        return -1;
    }
}

/*
https://leetcode.com/problems/search-in-rotated-sorted-array/solutions/14435/clever-idea-making-it-simple/
*/