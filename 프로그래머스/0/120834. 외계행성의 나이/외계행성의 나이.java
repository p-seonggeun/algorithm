import java.util.*;
class Solution {
    public String solution(int age) {
        String answer = "";
        StringBuilder sb = new StringBuilder();
        int[] i = Arrays.stream(String.valueOf(age).split(""))
            .mapToInt(Integer::parseInt)
            .toArray();
        for (int a : i) {
            sb.append((char) (a + 97));
        }
        answer = sb.toString();
        return answer;
    }
}