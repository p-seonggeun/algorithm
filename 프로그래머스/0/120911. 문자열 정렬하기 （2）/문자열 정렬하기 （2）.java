import java.util.*; 

class Solution {
    public String solution(String my_string) {
        char[] charArray = my_string.toCharArray();
        StringBuilder sb = new StringBuilder();

        for (char c : charArray) {
            if (Character.isUpperCase(c)) {
                sb.append(Character.toLowerCase(c));
            } else {
                sb.append(c);
            }
        }

        String string = sb.toString();
        String[] split = string.split("");
        Arrays.sort(split);
        
        String answer = String.join("", split);
        return answer;
    }
}