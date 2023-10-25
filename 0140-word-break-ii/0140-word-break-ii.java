class Solution {
    public List<String> wordBreak(String sentence, List<String> wordDict) {
        int n = sentence.length();
        List<List<String>>[] dp = new List[n + 1];
        dp[0] = new ArrayList<>();
        dp[0].add(new ArrayList<>());

        for (int i = 0; i <= n; i++) {
            if (dp[i] != null) {
                for (String word : wordDict) {
                    int m = word.length();
                    if (i + m <= n && sentence.substring(i, i + m).equals(word)) {
                        for (List<String> combination : dp[i]) {
                            List<String> newCombination = new ArrayList<>(combination);
                            newCombination.add(word);
                            if (dp[i + m] == null) {
                                dp[i + m] = new ArrayList<>();
                            }
                            dp[i + m].add(newCombination);
                        }
                    }
                }
            }
        }

        List<String> result = new ArrayList<>();
        if (dp[n] != null) {
            for (List<String> wordGroup : dp[n]) {
                result.add(String.join(" ", wordGroup));
            }
        }

        return result;
    }
}
