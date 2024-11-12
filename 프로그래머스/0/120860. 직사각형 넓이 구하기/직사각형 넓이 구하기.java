import java.util.*;

class Solution {
    public int solution(int[][] dots) {
        Arrays.sort(dots, new Comparator<int[]>() {
            @Override
            public int compare(int[] o1, int[] o2) {
                return o1[0] != o2[0] ? o1[0] - o2[0] : o1[1] - o2[1];
            }
        });

        int width = dots[3][0] - dots[0][0];
        int height = dots[3][1] - dots[0][1];

        int answer = width * height;
        return answer;
    }
}