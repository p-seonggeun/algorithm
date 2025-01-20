import java.util.*;

class Solution {
    public static int[] solution(int n, String[] words) {
        List<String> list = new ArrayList<>();

        for (int i = 0; i < words.length; i++) {
            if (list.contains(words[i])) {
                return new int[]{((i + 1) % n == 0) ? n : (i + 1) % n, i / n + 1};
            }

            if (i > 0 && words[i - 1].charAt(words[i - 1].length() - 1) != words[i].charAt(0)) {
                return new int[]{((i + 1) % n == 0) ? n : (i + 1) % n, i / n + 1};
            }

            list.add(words[i]);
        }

        return new int[]{0, 0};
    }
}