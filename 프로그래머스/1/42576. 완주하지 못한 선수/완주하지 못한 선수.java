import java.util.*;

class Solution {
    public String solution(String[] participant, String[] completion) {
        Map<String, Integer> map = new HashMap<>();

        for (String p : participant) {
            map.put(p, map.getOrDefault(p, 0) + 1);
        }

        for (String c : completion) {
            Integer value = map.get(c);
            if (--value == 0) {
                map.remove(c);
                continue;
            }
            map.put(c, value);
        }

        for (Map.Entry<String, Integer> entry : map.entrySet()) {
            return entry.getKey();
        }
        return null;
    }
}