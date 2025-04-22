import java.util.*;

class Solution {
    public long solution(long n) {
        long answer = 0;
        String[] temp = String.valueOf(n).split("");
        Arrays.sort(temp);
        String t = String.join("", temp);
        StringBuilder sb = new StringBuilder(t);
        sb.reverse();
        answer = Long.parseLong(sb.toString());
        return answer;
    }
}