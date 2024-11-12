import java.util.*;

class Solution {
    public String solution(String polynomial) {
        String[] split = polynomial.split(" ");
        int x = 0;
        int y = 0;

        for (String s : split) {
            if (s.contains("x")) {
                if (s.equals("x")) {
                    x += 1;
                } else {
                    x += Integer.parseInt(s.substring(0, s.length() - 1));
                }
            } else if (s.equals("+")) {
                continue;
            } else {
                y += Integer.parseInt(s);
            }
        }

        StringBuilder sb = new StringBuilder();
        if (x != 0) {
            if (x != 1) {
                sb.append(x);
            }
            sb.append("x");
        }
        if (y != 0) {
            if (sb.length() != 0) {
                sb.append(" + ");
            }
            sb.append(y);
        }

        String answer = sb.toString();
        return answer;
    }
}