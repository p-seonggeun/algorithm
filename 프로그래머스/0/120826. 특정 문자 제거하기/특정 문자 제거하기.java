import java.util.*;
class Solution {
    public String solution(String my_string, String letter) {
        String answer = "";
        StringBuilder sb = new StringBuilder();
        for (char c : my_string.toCharArray()) {
            if (!letter.equals(String.valueOf(c))) {
                sb.append(c);
            }
        }
        answer = sb.toString();
        return answer;
    }
}