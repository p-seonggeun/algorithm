import java.util.*;

class Solution {
    public static int[] solution(String[] id_list, String[] report, int k) {
        Map<String, HashSet<String>> map = new HashMap<>();
        Map<String, Integer> index = new HashMap<>();
        int[] count = new int[id_list.length];
        HashSet<String> reportMember = new HashSet<>();

        for (int i = 0; i < id_list.length; i++) {
            index.put(id_list[i], i);
        }

        for (String r : report) {
            String[] split = r.split(" ");
            HashSet<String> value = map.getOrDefault(split[0], new HashSet<>());
            int before = value.size();
            value.add(split[1]);
            int after = value.size();
            map.put(split[0], value);

            if (before != after) {
                count[index.get(split[1])]++;
            }

            if (count[index.get(split[1])] >= k) {
                reportMember.add(split[1]);
            }
        }

        int[] answer = new int[id_list.length];
        for (int i = 0; i < id_list.length; i++) {
            HashSet<String> target = map.get(id_list[i]);
            if (target != null) {
                target.retainAll(reportMember);
                answer[index.get(id_list[i])] = target.size();
            }
        }
        return answer;
    }
}