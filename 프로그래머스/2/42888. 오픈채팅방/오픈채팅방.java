import java.util.*;

class Solution {
    public static String[] solution(String[] records) {
        Map<String, String> map = new HashMap<>();
        List<String> list = new ArrayList<>();
        for (String record : records) {
            String[] split = record.split(" ");
            if (split[0].equals("Enter")) {
                map.put(split[1], split[2]);
                list.add(split[1] + "님이 들어왔습니다.");
            }

            if (split[0].equals("Leave")) {
                list.add(split[1] + "님이 나갔습니다.");
            }

            if (split[0].equals("Change")) {
                map.put(split[1], split[2]);
            }
        }

        List<String> temp = new ArrayList<>();
        for (String s : list) {
            int hashIndex = s.indexOf("님");
            String uid = s.substring(0, hashIndex);
            String command = s.substring(hashIndex);
            String nickname = map.get(uid);
            temp.add(nickname + command);
        }

        String[] answer = temp.toArray(String[]::new);
        return answer;
    }
}