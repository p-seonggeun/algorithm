import java.util.*;

class Solution {
    public int solution(int[] array, int n) {
        int minus = Integer.MAX_VALUE;
        int answer = 0;
        Arrays.sort(array);

        for (int arr : array) {
            if (Math.abs(arr - n) < minus) {
                minus = Math.abs(arr - n);
                answer = arr;
            }
        }
        
        return answer;
    }
}