import java.util.*;

class Solution {
    private static final int[] dx = {-1, -1, -1, 0, 1, 1, 1, 0};
    private static final int[] dy = {-1, 0, 1, 1, 1, 0, -1, -1};
    
    public int solution(int[][] board) {
        int[][] visited = new int[board.length][board.length];

        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board.length; j++) {
                if (board[i][j] == 1 && visited[i][j] == 0) {
                    bfs(board, i, j, visited);
                }
            }
        }
        
        int answer = count(board);
        return answer;
    }
    
    public static int count(int[][] map) {
        int answer = 0;
        for (int i = 0; i < map.length; i++) {
            for (int j = 0; j < map.length; j++) {
                if (map[i][j] == 0) {
                    answer++;
                }
            }
        }
        return answer;
    }

    public static void bfs(int[][] map, int i, int j, int[][] visited) {
        Queue<Integer[]> queue = new ArrayDeque<>();
        queue.add(new Integer[]{i, j});
        int width = map.length;
        int height = width;
        while (!queue.isEmpty()) {
            Integer[] remove = queue.remove();
            int x = remove[0];
            int y = remove[1];

            for (int k = 0; k < 8; k++) {
                int nx = x + dx[k];
                int ny = y + dy[k];

                if (0 <= nx && nx < width && 0 <= ny && ny < height) {
                    if (map[nx][ny] == 0 && visited[nx][ny] == 0) {
                        map[nx][ny] += 1;
                        visited[nx][ny] = 1;
                    }
                }
            }
        }
    }
}