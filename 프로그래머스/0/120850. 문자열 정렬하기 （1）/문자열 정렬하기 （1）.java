import java.util.*;
class Solution {
    public int[] solution(String my_string) {
        List<Integer> list = new ArrayList<>();

        for (int i = 0; i < my_string.length(); i++) {
            if (Character.isDigit(my_string.charAt(i))) {
                String s = String.valueOf(my_string.charAt(i));
                list.add(Integer.valueOf(s));
            }
        }
        
        Collections.sort(list);
        return list.stream().mapToInt(Integer::intValue).toArray();
    }
}