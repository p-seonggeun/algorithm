import java.lang.Math;
import java.util.*;

class Solution {
    public int[] solution(int[] arr, int[][] queries) {
        int[] answer = {};
        List<Integer> list = new ArrayList<>();
        
        for (int[] query : queries) {
            int s = query[0];
            int e = query[1];
            int k = query[2];
            
            int min = 999_999_999;
            for (int a : Arrays.copyOfRange(arr, s, e + 1)) {
                if (a > k) {
                    min = Math.min(min, a);
                }
            }
            if (min == 999_999_999) {
                list.add(-1);
            } else {
               list.add(min); 
            }
        }
        answer = list.stream()
            .mapToInt(i -> i)
            .toArray();
        return answer;
    }
}