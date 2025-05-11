import java.util.*;

class Solution {
    public String solution(int[] numbers) {
        String answer = "";
        
        String[] str = Arrays.stream(numbers)
            .mapToObj(n -> String.valueOf(n))
            .toArray(String[]::new);
        
        Arrays.sort(str, new Comparator<String>() {
            public int compare(String s1, String s2) {
                return (s2 + s1).compareTo(s1 + s2);
            }
        });
        
        answer = String.join("", str);
        if (answer.startsWith("0")) {
            return "0";
        }
        
        return answer;
    }
}