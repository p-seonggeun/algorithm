import java.util.*;

class Solution {
    public int solution(int[][] board, int[] moves) {
        int answer = 0;
        ArrayDeque<Integer> stack = new ArrayDeque<>();
        int N = board.length;

        for (int move : moves) {
            for (int i = 0; i < N; i++) {
                if (board[i][move - 1] != 0) {
                    int target = board[i][move - 1];
                    if (check(target, stack)) {
                        answer++;
                    }
                    board[i][move - 1] = 0;
                    break;
                }
            }
        }

        return answer * 2;
    }

    public static boolean check(int target, ArrayDeque<Integer> stack) {
        if (stack.isEmpty()) {
            stack.addLast(target);
            return false;
        }

        if (stack.peekLast() == target) {
            stack.pollLast();
            return true;
        }

        stack.addLast(target);
        return false;
    }
}