import java.util.*;

class Solution {
public static int solution(String s) {
        ArrayDeque<Character> stack = new ArrayDeque<>();
        for (char c : s.toCharArray()) {
            if (stack.isEmpty()) {
                stack.addLast(c);
            } else {
                if (c == stack.peekLast()) {
                    stack.pollLast();
                } else {
                    stack.addLast(c);
                }
            }
        }

        if (stack.isEmpty()) {
            return 1;
        }
        return 0;
    }
}