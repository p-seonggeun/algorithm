class Solution {
    public int solution(int n, int k) {
        int answer = 0;
        int a = n / 10;
        
        int b = (a > k) ? 0 : k - a;
        
        answer = 12_000 * n + b * 2_000;
        return answer;
    }
}