class Solution {
    public List<Integer> intersection(int[][] nums) {
        Map<Integer, Integer> map = new HashMap<>();
        List<Integer> result  = new ArrayList<>();

        for(int[] row : nums){
            for(int num : row){
               map.put(num, map.getOrDefault(num, 0) + 1);
            }
        }

        for(int key : map.keySet()){
            if(map.get(key) == nums.length){
                result.add(key);
            }
        }
        
        Collections.sort(result);
        return result;
    }
}