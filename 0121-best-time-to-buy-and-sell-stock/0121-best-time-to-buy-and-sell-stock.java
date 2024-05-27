class Solution {
    public int maxProfit(int[] prices) {
        int maxProfit = 0;
        int buyingPrice = prices[0];

        for (int sellingPrice: prices){
            buyingPrice = Math.min(buyingPrice, sellingPrice);
            maxProfit = Math.max(maxProfit, sellingPrice - buyingPrice);
        }

        return maxProfit;
    }
}