import java.util.*;

class Solution {
    public static int rank = 1;
    public static int[] solution(int[][] score) {
        List<Integer> list = new ArrayList<>();
        for (int[] s : score) {
            Integer integer = (s[0] + s[1]);
            list.add(integer);
        }

        list.sort(Collections.reverseOrder());
        System.out.println(list);

        int[] answer = new int[score.length];
        for (int i = 0; i < score.length; i++) {
            System.out.println(i);
            int standard = list.get(i);
            int count = 0;
            for (int j = 0; j < score.length; j++) {
                if (standard == score[j][0] + score[j][1]) {
                    answer[j] = rank;
                    count++;
                }
            }
            if (i != score.length - 1 && (Objects.equals(list.get(i), list.get(i + 1)))) {
                continue;
            }
            rank += count;
        }
        return answer;
    }
}