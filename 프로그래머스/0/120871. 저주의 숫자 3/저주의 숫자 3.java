class Solution {
    public static int solution(int n) {
        int[] dp = new int[101];

        for (int i = 1; i < dp.length; i++) {
            dp[i] = dp[i - 1] + 1;
            while (dp[i] % 3 == 0 || String.valueOf(dp[i]).contains("3")) {
                dp[i] += 1;
            }
        }
        
        return dp[n];
    }
}