class Solution {
    public int gcd(int a, int b) {
        if (b == 0) {
            return a;
        } else {
            return gcd(b, a % b);
        }
    }
    
    public int solution(int n) {
        int answer = 0;
        int g = 0;
        
        if (n >= 6) {
            g = gcd(n, 6);
        } else {
            g = gcd(6, n);
        }
        
        answer = (n * 6) / g / 6;
        return answer;
    }
}