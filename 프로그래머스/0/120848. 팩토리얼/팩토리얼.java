class Solution {
    public int solution(int n) {
        if (n == 1) {
            return 1;
        }
        int answer = 0;
        int t = 1;
        for (int i = 1; i <= 10; i++) {
            if (t > n) {
                return answer - 1;
            } else if (t == n) {
                return answer;
            }
            t *= i;
            answer++;
        }
        return answer;
    }
}