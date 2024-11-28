import java.util.*;

class Solution {
    public static int solution(String s) {
        int answer = 0;
        List<Character> list = new ArrayList<>();
        char[] charArray = s.toCharArray();
        for (char c : charArray) {
            list.add(c);
        }

        for (int i = 0; i < list.size(); i++) {
            if (i != 0) {
                Collections.rotate(list, -1);
            }
            char[] chars = new char[list.size()];
            for (int j = 0; j < list.size(); j++) {
                chars[j] = list.get(j);
            }
            if (check(chars)) {
                answer++;
            }
        }
        return answer;
    }

    public static boolean check(char[] chars) {
        ArrayDeque<Character> stack = new ArrayDeque<>();

        for (char c : chars) {
            if (c == '(' || c == '[' || c == '{') {
                stack.addLast(c);
            } else {
                if (stack.isEmpty()) {
                    return false;
                } else if (c == ')' && stack.peekLast() == '(') {
                    stack.pollLast();
                } else if (c == ']' && stack.peekLast() == '[') {
                    stack.pollLast();
                } else if (c == '}' && stack.peekLast() == '{') {
                    stack.pollLast();
                }
            }
        }
        return stack.isEmpty();
    }
}