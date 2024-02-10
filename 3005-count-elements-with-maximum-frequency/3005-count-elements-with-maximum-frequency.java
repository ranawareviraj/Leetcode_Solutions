class Solution {
    public int maxFrequencyElements(int[] nums) {
        Map<Integer, Integer> map = new HashMap<>();
        int maxFreq = 0;
        for(int num : nums){
            int freq = map.getOrDefault(num, 0) + 1;
            map.put(num, freq);
            maxFreq = Math.max(maxFreq, freq);
        }

        int ans = 0;
        for(int num : map.keySet()){
            if (map.get(num) == maxFreq){
                ans += maxFreq;
            }
        }

        return ans;
    }
}
