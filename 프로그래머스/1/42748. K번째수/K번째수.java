import java.util.*;

class Solution {
    public static int[] solution(int[] array, int[][] command) {
        List<Integer> list = new ArrayList<>();
        for (int[] ints : command) {
            int i = ints[0];
            int j = ints[1];
            int k = ints[2];

            int[] ints1 = Arrays.copyOfRange(array, i - 1, j);
            Arrays.sort(ints1);
            list.add(ints1[k - 1]);
        }

        return list.stream()
                .mapToInt(i -> i).toArray();
    }
}