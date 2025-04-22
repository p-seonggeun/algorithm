import java.util.*;

class Solution {
    public double solution(int[] arr) {
        double answer = 0;
        int temp = Arrays.stream(arr)
            .sum();
        answer = (double) temp / arr.length;
        return answer;
    }
}