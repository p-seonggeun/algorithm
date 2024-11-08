import java.util.*;

class Solution {
    public String[] solution(String[] quiz) {
        List<String> list = new ArrayList<>();
        for (String q : quiz) {
            String[] split = q.split(" = ");
            String ans = split[1];
            int expression = expression(split[0]);
            if (expression == Integer.parseInt(ans)) {
                list.add("O");
            } else {
                list.add("X");
            }
        }

        String[] answer = list.toArray(String[]::new);
        return answer;
    }
    
    public static int expression(String my_string) {
        int answer = 0;
        boolean plus = true;

        String[] split = my_string.split(" ");
        for (String s : split) {
            if (Character.isDigit(s.charAt(0)) || s.length() >= 2) {
                if (plus) {
                    answer += Integer.parseInt(s);
                } else {
                    answer -= Integer.parseInt(s);
                }
            } else {
                if (s.equals("+")) {
                    plus = true;
                } else {
                    plus = false;
                }
            }
        }

        return answer;
    }
}