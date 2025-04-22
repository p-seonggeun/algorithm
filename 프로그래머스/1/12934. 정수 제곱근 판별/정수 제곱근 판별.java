import java.lang.Math;

class Solution {
    public long solution(long n) {
        long answer = 0;
        double temp = Math.sqrt(n);
        
        if (temp == (int) temp) {
            return (long) Math.pow(temp + 1, 2);
        } else {
            return -1;
        }
    }
}