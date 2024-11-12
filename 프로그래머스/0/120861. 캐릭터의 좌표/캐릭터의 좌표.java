import java.util.*;

class Solution {
    public int[] solution(String[] keyinput, int[] board) {
        int[] answer = {0, 0};
        Map<String, Integer[]> map = new HashMap<>(Map.of(
                        "up", new Integer[]{0, 1},
                        "down", new Integer[]{0, -1},
                        "left", new Integer[]{-1, 0},
                        "right", new Integer[]{1, 0}));
        int maxX = (board[0] - 1) / 2;
        int minX = -maxX;
        int maxY = (board[1] - 1) / 2;
        int minY = -maxY;

        for (String key : keyinput) {
            Integer[] move = map.get(key);
            int dx = move[0];
            int dy = move[1];
            if (answer[0] + dx >= minX && answer[0] + dx <= maxX && 
                answer[1] + dy >= minY && answer[1] + dy <= maxY) {
                answer[0] += dx;
                answer[1] += dy;
            }
        }

        return answer;
    }
}