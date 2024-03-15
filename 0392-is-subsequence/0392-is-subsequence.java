class Solution {
    public boolean isSubsequence(String s, String t) {
        int sLength = s.length(), tLength = t.length();
        int i = 0, j = 0;

        while(i < sLength && j < tLength){
            if (s.charAt(i) == t.charAt(j)){
                i += 1;
            }
            j += 1;
        }

        return i == s.length();
    }
}