class Solution {
    public String mergeAlternately(String word1, String word2) {
        StringBuilder sb = new StringBuilder();
        int l1 = word1.length();
        int l2 = word2.length();
        int p1 = 0;
        int p2 = 0;

        while (p1 < l1 || p2 < l2) {
            if (p1 < l1) {
                sb.append(word1.charAt(p1));
            }

            if (p2 < l2) {
                sb.append(word2.charAt(p2));
            }

            p1 += 1;
            p2 += 1;
        }

        return sb.toString();
    }
}