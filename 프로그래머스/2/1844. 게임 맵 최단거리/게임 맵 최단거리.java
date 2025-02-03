import java.util.*;

class Solution {
    public static int[] dx = new int[]{-1, 1, 0, 0};
    public static int[] dy = new int[]{0, 0, -1, 1};

    public static int solution(int[][] maps) {
        int n = maps.length;
        int m = maps[0].length;

        ArrayDeque<Integer[]> queue = new ArrayDeque<>();
        queue.addLast(new Integer[]{0, 0});

        while (!queue.isEmpty()) {
            Integer[] poll = queue.pollFirst();
            Integer x = poll[0];
            Integer y = poll[1];

            for (int i = 0; i < 4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];

                if (0 <= nx && nx < n && 0 <= ny && ny < m) {
                    if (maps[nx][ny] == 1) {
                        maps[nx][ny] = maps[x][y] + 1;
                        queue.addLast(new Integer[]{nx, ny});
                    }
                }
            }
        }

        return maps[n - 1][m - 1] != 1 ? maps[n - 1][m - 1] : -1;
    }
}