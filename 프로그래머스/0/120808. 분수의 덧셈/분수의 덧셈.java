class Solution {
    public int gcd(int a, int b) {
        if (b == 0) {
            return a;
        } else {
            return gcd(b, a % b);
        }
    }
    
    public int[] solution(int numer1, int denom1, int numer2, int denom2) {
        int[] answer = {};
        int a = (numer1 * denom2) + (numer2 * denom1);
        int b = (denom1 * denom2);
        int g = gcd(a, b);
        
        answer = new int[] {(a / g), (b / g)};
        
        return answer;
    }
}