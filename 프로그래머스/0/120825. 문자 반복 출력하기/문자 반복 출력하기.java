import java.util.*;
class Solution {
    public String solution(String my_string, int n) {
        String answer = "";
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < my_string.length(); i++) {
            String t = String.valueOf(my_string.charAt(i));
            sb.append(t.repeat(n));
        }
        answer = sb.toString();
        return answer;
    }
}