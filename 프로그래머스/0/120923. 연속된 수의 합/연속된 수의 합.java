import java.util.*;

class Solution {
    public static int[] solution(int num, int total) {
        List<Integer> list = new ArrayList<>();
        int mid = total / num;
        int start = total % num == 0 ? -(num / 2) : -(num / 2 - 1);
        start = start + mid;
        for (int i = 0; i < num; i++) {
            list.add(start + i);
        }
        
        return list.stream()
            .mapToInt(i -> i)
            .toArray();
    }
}