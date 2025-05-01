class Solution {
    public int solution(int n) {
        int answer = 0;
        
        for (int i = 1; i <= n; i++) {
            if (is(i, n)) {
                answer++;
            }
        }
        return answer;
    }
    
    public boolean is(int i, int n) {
        int temp = 0;
        for (int j = i; i <= n; j++) {
            temp += j;
            if (temp == n) {
                return true;
            }
            if (temp > n) {
                return false;
            }
        }
        return false;
    }
}