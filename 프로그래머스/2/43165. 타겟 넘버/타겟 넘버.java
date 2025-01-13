import java.util.*;

class Solution {
    public static int solution(int[] numbers, int target) {
        int[] answer = {0};
        String[] operation = new String[]{"+", "-"};
        dfs(operation, numbers, target, 0, new ArrayList<>(), answer);
        return answer[0];
    }

    public static void dfs(String[] operation, int[] numbers, int target, int count, List<Integer> now, int[] answer) {
        if (count == numbers.length) {
            int sum = now.stream()
                    .mapToInt(Integer::intValue)
                    .sum();
            if (sum == target) {
                answer[0]++;
            }
            return;
        }

        for (int i = 0; i < operation.length; i++) {
            int number = numbers[count];
            if (operation[i].equals("-")) {
                number = -number;
            }

            now.add(number);
            dfs(operation, numbers, target, count + 1, now, answer);
            now.remove(now.size() - 1);
        }
    }
}