import java.util.*;

class Solution {
    public static int[] solution(int N, int[] stages) {
        List<Number[]> list = new ArrayList<>();
        for (int i = 1; i <= N; i++) {
            int total = 0;
            int fail = 0;
            double failure = 0.0;
            for (int stage : stages) {
                if (i <= stage) {
                    total++;
                    if (i >= stage) {
                        fail++;
                    }
                }
            }
            if (total == 0) {
                failure = 0;
            } else {
                failure = (double) fail / total;
            }
            list.add(new Number[]{i, failure});
        }
        list.sort(new Comparator<Number[]>() {
            @Override
            public int compare(Number[] o1, Number[] o2) {
                int compare = Double.compare((double) o2[1], (double) o1[1]);
                if (compare != 0) {
                    return compare;
                }
                return Integer.compare((int) o1[0], (int) o2[0]);
            }
        });
        
        int[] answer = new int[N];
        for (int i = 0; i < N; i++) {
            Number[] numbers = list.get(i);
            answer[i] = (int) numbers[0];
        }
        return answer;
    }
}