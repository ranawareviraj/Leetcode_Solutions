class Solution {
    public boolean isAnagram(String s, String t) {
        Map<Character, Integer> sMap = new HashMap<>();
        for(char ch: s.toCharArray()){
            sMap.put(ch, sMap.getOrDefault(ch, 0) + 1);
        }

        for (char ch : t.toCharArray()) {
            if(!sMap.containsKey(ch)){
                return false;
            }

            sMap.put(ch, sMap.get(ch) - 1);
            if(sMap.get(ch) == 0){
                sMap.remove(ch);
            }
        }

        return sMap.isEmpty();
    }
}