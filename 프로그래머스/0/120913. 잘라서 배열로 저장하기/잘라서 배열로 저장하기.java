import java.util.*;

class Solution {
    public String[] solution(String my_str, int n) {
        StringBuilder sb = new StringBuilder();
        List<String> temp = new ArrayList<>();

        String[] split = my_str.split("");
        for (String s : split) {
            sb.append(s);
            if (sb.length() == n) {
                temp.add(sb.toString());
                sb.setLength(0);
            }
        }
        
        if (sb.length() != 0) {
            temp.add(sb.toString());
        }
        
        String[] answer = temp.toArray(String[]::new);
        return answer;
    }
}