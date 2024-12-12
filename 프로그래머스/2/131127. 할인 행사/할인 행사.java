import java.util.*;

class Solution {
    public static int solution(String[] want, int[] number, String[] discount) {
        Map<String, Integer> map = new HashMap<>();
        Map<String, Integer> real = new HashMap<>();

        int answer = 0;

        for (int i = 0; i < want.length; i++) {
            map.put(want[i], number[i]);
        }

        int s = 0;
        int e = 9;

        for (int i = 0; i < discount.length - 10 + 1; i++) {
            if (i == 0) {
                for (int j = 0; j < 10; j++) {
                    real.put(discount[j], real.getOrDefault(discount[j], 0) + 1);
                }
                if (map.equals(real)) {
                    answer++;
                }
                continue;
            }

            Integer count = real.get(discount[s]);
            if (--count == 0) {
                real.remove(discount[s]);
            } else {
                real.put(discount[s], count);
            }
            s++;
            e++;

            real.put(discount[e], real.getOrDefault(discount[e], 0) + 1);

            if (map.equals(real)) {
                answer++;
            }
        }

        return answer;
    }
}