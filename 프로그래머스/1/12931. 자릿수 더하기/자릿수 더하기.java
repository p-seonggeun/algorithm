import java.util.*;

public class Solution {
    public int solution(int n) {
        int answer = 0;
        String temp = String.valueOf(n);
        for (int i = 0; i < temp.length(); i++) {
            answer += Integer.valueOf(temp.charAt(i)) - 48;
        }

        return answer;
    }
}