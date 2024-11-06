import java.util.*;

class Solution {
    public String solution(String my_string) {
        List<String> answer = new ArrayList<>();
        
        for (int i = 0; i < my_string.length(); i++) {
            if (!answer.contains(String.valueOf(my_string.charAt(i)))) {
                answer.add(String.valueOf(my_string.charAt(i)));
            }
        }
        
        return String.join("", answer);
    }
}