import java.util.*;

class Solution {
    public static String solution(String[] id_pw, String[][] db) {
        HashMap<String, String> map = new HashMap<>();
        for (String[] strings : db) {
            map.put(strings[0], strings[1]);
        }

        if (map.containsKey(id_pw[0])) {
            if (map.get(id_pw[0]).equals(id_pw[1])) {
                return "login";
            }
            return "wrong pw";
        }
        return "fail";
    }
}