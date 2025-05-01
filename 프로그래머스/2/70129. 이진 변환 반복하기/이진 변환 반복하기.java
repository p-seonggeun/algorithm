import java.util.*;

class Solution {
    public int[] solution(String s) {
        int[] answer = {0, 0};
        
        while (!s.equals("1")) {
            answer[0] += 1;
            int first = s.length();
            s = s.replaceAll("0", "");
            int second = s.length();
            answer[1] += first - second;
            s = bin(s.length());
        }
        return answer;
    }
    
    public String bin(int s) {
        return Integer.toBinaryString(s);
    }
}