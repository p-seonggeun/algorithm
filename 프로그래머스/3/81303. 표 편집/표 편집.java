import java.util.*;

class Solution {
    
    static class Node {
        int index;
        Node prev;
        Node next;

        public Node(int index) {
            this.index = index;
        }

    }

    public static String solution(int n, int k, String[] cmd) {
        ArrayDeque<Node> stack = new ArrayDeque<>();
        Node[] table = new Node[n];
        for (int i = 0; i < n; i++) {
            table[i] = new Node(i);
        }

        for (int i = 0; i < n; i++) {
            if (i > 0) {
                table[i].prev = table[i - 1];
            }
            if (i < n - 1) {
                table[i].next = table[i + 1];
            }
        }

        Node nowNode = table[k];
        for (String command : cmd) {
            if (command.charAt(0) == 'C') {
                stack.addLast(nowNode);
                if (nowNode.prev == null) {
                    nowNode.next.prev = null;
                    nowNode = nowNode.next;
                } else if (nowNode.next == null) {
                    nowNode.prev.next = null;
                    nowNode = nowNode.prev;
                } else {
                    nowNode.prev.next = nowNode.next;
                    nowNode.next.prev = nowNode.prev;
                    nowNode = nowNode.next;
                }
            } else if (command.charAt(0) == 'Z') {
                Node rollbackNode = stack.pollLast();
                if (rollbackNode.prev == null) {
                    rollbackNode.next.prev = rollbackNode;
                } else if (rollbackNode.next == null) {
                    rollbackNode.prev.next = rollbackNode;
                } else {
                    rollbackNode.next.prev = rollbackNode;
                    rollbackNode.prev.next = rollbackNode;
                }
            } else {
                Integer move = Integer.valueOf(command.substring(2));
                if (command.charAt(0) == 'U') {
                    for (int i = 0; i < move; i++) {
                        nowNode = nowNode.prev;
                    }
                }
                else {
                    for (int i = 0; i < move; i++) {
                        nowNode = nowNode.next;
                    }
                }
            }
        }

        String[] answer = new String[n];
        Arrays.fill(answer, "O");
        for (Node node : stack) {
            answer[node.index] = "X";
        }

        return String.join("", answer);
    }
}