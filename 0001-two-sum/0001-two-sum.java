class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> seen = new HashMap<>();

        for (int i = 0; i < nums.length; i++){
            int num = nums[i];
            int numToLookup = target - num;
            
            if(seen.containsKey(numToLookup)){
                return new int[]{i, seen.get(numToLookup)};
            }

            seen.put(num, i);
        }

        return new int[]{-1, -1};
    }
}