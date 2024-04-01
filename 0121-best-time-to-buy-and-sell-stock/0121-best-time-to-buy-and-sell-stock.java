class Solution {
    public int maxProfit(int[] prices) {
        int buyingPrice = prices[0];
        int maxProfit = 0;

        for (int currentPrice : prices) {
            maxProfit = Math.max(maxProfit, currentPrice - buyingPrice);
            if (currentPrice < buyingPrice) {
                buyingPrice = currentPrice;
            }
        }

        return maxProfit;
    }
}