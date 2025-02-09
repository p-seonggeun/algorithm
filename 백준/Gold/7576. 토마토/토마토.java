import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Arrays;

public class Main {

    public static int[] dx = {-1, 1, 0, 0};
    public static int[] dy = {0, 0, -1, 1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] split = br.readLine().split(" ");
        int M = Integer.parseInt(split[0]);
        int N = Integer.parseInt(split[1]);
        int[][] map = new int[N][M];

        for (int i = 0; i < N; i++) {
            String[] info = br.readLine().split(" ");
            int[] array = Arrays.stream(info)
                    .mapToInt(s -> Integer.parseInt(s)).toArray();

            map[i] = array;
        }

        boolean bfs = false;

        ArrayDeque<Integer[]> queue = new ArrayDeque<>();
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (map[i][j] == 0) {
                    bfs = true;
                }
                if (map[i][j] == 1) {
                    queue.add(new Integer[]{i, j});
                }
            }
        }

        if (bfs) {
            while (!queue.isEmpty()) {
                Integer[] pop = queue.pop();
                int x = pop[0];
                int y = pop[1];

                for (int i = 0; i < 4; i++) {
                    int nx = x + dx[i];
                    int ny = y + dy[i];

                    if (0 <= nx && nx < N && 0 <= ny && ny < M) {
                        if (map[nx][ny] == 0) {
                            map[nx][ny] = map[x][y] + 1;
                            queue.add(new Integer[]{nx, ny});
                        }
                    }
                }
            }
        }

        int result = 0;
        boolean answer = true;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (map[i][j] == 0) {
                    answer = false;
                }
                result = Integer.max(result, map[i][j]);
            }
        }

        if (answer) {
            System.out.println(result - 1);
        } else {
            System.out.println(-1);
        }
    }
}