import java.util.*;

class Solution {
    public String solution(String s) {
        String[] split = s.split("");
        HashMap<String, Integer> map = new HashMap<>();

        for (String arr : split) {
            map.put(arr, map.getOrDefault(arr, 0) + 1);
        }

        StringBuilder sb = new StringBuilder();
        Set<String> strings = map.keySet();
        for (String string : strings) {
            if (map.get(string) == 1) {
                sb.append(string);
            }
        }

        String string = sb.toString();
        String[] sp = string.split("");
        Arrays.sort(sp);
        String answer = String.join("", sp);
        
        return answer;
    }
}