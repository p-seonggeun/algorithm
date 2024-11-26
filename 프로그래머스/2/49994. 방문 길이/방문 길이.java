import java.util.*;

class Solution {
    public static int solution(String dirs) {
        int answer = 0;
        String[] split = dirs.split("");
        int[] character = {0, 0};
        List<List<Integer>> check = new ArrayList<>();
        for (String s : split) {
            int dx = 0;
            int dy = 0;
            if (s.equals("U")) {
                dx = 0;
                dy = 1;
            } else if (s.equals("D")) {
                dx = 0;
                dy = -1;
            } else if (s.equals("L")) {
                dx = -1;
                dy = 0;
            } else if (s.equals("R")) {
                dx = 1;
                dy = 0;
            }

            int nx = character[0] + dx;
            int ny = character[1] + dy;

            if (-5 <= nx && nx <= 5 && -5 <= ny && ny <= 5) {
                List<Integer> move = Arrays.asList(character[0], character[1], nx, ny);
                List<Integer> reverse = Arrays.asList(nx, ny, character[0], character[1]);

                if (!check.contains(move) && !check.contains(reverse)) {
                    check.add(move);
                    check.add(reverse);
                    answer++;
                }
                character[0] = nx;
                character[1] = ny;
            }
        }
        return answer;
    }
}