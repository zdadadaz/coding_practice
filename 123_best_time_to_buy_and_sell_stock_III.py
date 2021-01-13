class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sell1 = sell2 = 0
        buy1 = buy2 = -float('inf')
        for p in prices:
            buy1 = max(buy1, -p)
            sell1 = max(sell1, buy1 + p)
            buy2 = max(buy2, sell1 - p)
            sell2 = max(sell2, buy2 + p)
        return sell2

# 2D DP
# class Solution {
# public:
#     int maxProfit(vector<int> &prices) {
#         if (prices.empty()) return 0;
#         int n = prices.size(), g[n][3] = {0}, l[n][3] = {0};
#         for (int i = 1; i < prices.size(); ++i) {
#             int diff = prices[i] - prices[i - 1];
#             for (int j = 1; j <= 2; ++j) {
#                 l[i][j] = max(g[i - 1][j - 1] + max(diff, 0), l[i - 1][j] + diff);
#                 g[i][j] = max(l[i][j], g[i - 1][j]);
#             }
#         }
#         return g[n - 1][2];
#     }
# };

# 1D DP
# class Solution {
# public:
#     int maxProfit(vector<int> &prices) {
#         if (prices.empty()) return 0;
#         int g[3] = {0};
#         int l[3] = {0};
#         for (int i = 0; i < prices.size() - 1; ++i) {
#             int diff = prices[i + 1] - prices[i];
#             for (int j = 2; j >= 1; --j) {
#                 l[j] = max(g[j - 1] + max(diff, 0), l[j] + diff);
#                 g[j] = max(l[j], g[j]);
#             }
#         }
#         return g[2];
#     }
# };