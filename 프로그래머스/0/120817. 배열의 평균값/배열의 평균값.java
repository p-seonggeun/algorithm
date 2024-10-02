import java.util.*;

class Solution {
    public double solution(int[] numbers) {
        double answer = 0;
        int hap = Arrays.stream(numbers).sum();
        answer = (double) hap / numbers.length;
        return answer;
    }
}