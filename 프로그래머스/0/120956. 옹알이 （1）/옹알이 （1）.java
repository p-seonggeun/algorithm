import java.util.*;
class Solution {
    public static int solution(String[] babbling) {
        String[] can = new String[]{"aya", "ye", "woo", "ma"};
        int answer = 0;
        for (String b : babbling) {
            for (String s : can) {
                if (b.contains(s)) {
                    b = b.replace(s, "1");
                }
            }
            b = b.replace("1", "");
            if (b.isBlank()) {
                answer++;
            }
        }
        return answer;
    }
}