import java.util.*;

class Solution {
    public int[] solution(long n) {
        int[] answer = {};
        String temp = String.valueOf(n);
        StringBuilder sb = new StringBuilder(temp);
        sb.reverse();
        
        String[] temp2 = sb.toString().split("");
        answer = Arrays.stream(temp2)
            .mapToInt(t -> Integer.valueOf(t))
            .toArray();
        
        return answer;
    }
}