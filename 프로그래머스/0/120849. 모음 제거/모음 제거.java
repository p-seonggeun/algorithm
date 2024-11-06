import java.util.*;
class Solution {
    public String solution(String my_string) {
        StringBuilder sb = new StringBuilder();
        List<Character> list = new ArrayList<>(List.of('a', 'e', 'i', 'o', 'u'));
        
        for (int i = 0; i < my_string.length(); i++) {
            if (!list.contains(my_string.charAt(i))) {
                sb.append(my_string.charAt(i));
            }
        }
        
        return sb.toString();
    }
}