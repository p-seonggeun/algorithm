import java.util.*;

class Solution {
    public static int[][] solution(int[][] nodeinfo) {
        List<Node> list = new ArrayList<>();
        List<Integer> temp = new ArrayList<>();
        for (int i = 0; i < nodeinfo.length; i++) {
            int x = nodeinfo[i][0];
            int y = nodeinfo[i][1];
            Node node = new Node(i + 1, x, y);
            list.add(node);

            if (!temp.contains(y)) {
                temp.add(y);
            }
        }

        Map<Integer, List<Node>> heightOfNode = new HashMap<>();
        for (Node node : list) {
            int y = node.getY();
            List<Node> nodeList = heightOfNode.getOrDefault(y, new ArrayList<>());
            nodeList.add(node);
            nodeList.sort(new Comparator<Node>() {
                @Override
                public int compare(Node o1, Node o2) {
                    return o1.getX() - o2.getX();
                }
            });
            heightOfNode.put(y, nodeList);
        }

        temp.sort(Collections.reverseOrder());
        int[] heights = temp.stream().mapToInt(h -> h).toArray();

        Node rootNode = heightOfNode.get(heights[0]).get(0);
        for (int i = 1; i < heights.length; i++) {
            List<Node> nodes = heightOfNode.get(heights[i]);
            for (Node node : nodes) {
                rootNode.addChild(node);
            }
        }

        List<Integer> preOrder = new ArrayList<>();
        preOrder(preOrder, rootNode);
        
        List<Integer> postOrder = new ArrayList<>();
        postOrder(postOrder, rootNode);

        int[] pre = preOrder.stream().mapToInt(i -> i).toArray();
        int[] post = postOrder.stream().mapToInt(i -> i).toArray();

        int[][] answer = {pre, post};
        return answer;
    }

    public static void preOrder(List<Integer> preOrder, Node node) {
        if (node == null) {
            return;
        }
        if (!preOrder.contains(node)) {
            preOrder.add(node.index);
        }
        preOrder(preOrder, node.leftChild);
        preOrder(preOrder, node.rightChild);
    }

    public static void postOrder(List<Integer> postOrder, Node node) {
        if (node == null) {
            return;
        }
        postOrder(postOrder, node.leftChild);
        postOrder(postOrder, node.rightChild);
        if (!postOrder.contains(node)) {
            postOrder.add(node.index);
        }
    }
    
    
    static class Node {
        private final int index;
        private final int x;
        private final int y;

        private Node leftChild;
        private Node rightChild;

        public Node(int index, int x, int y) {
            this.index = index;
            this.x = x;
            this.y = y;
        }

        public void addChild(Node child) {
            if (child.getX() < this.x) { // 왼쪽 자식일 때
                if (this.leftChild == null) { // 왼쪽 자식이 비어있을 때
                    this.leftChild = child;
                } else {
                    this.leftChild.addChild(child);
                }
            } else { // 오른쪽 자식일 때
                if (this.rightChild == null) {
                    this.rightChild = child;
                } else {
                    this.rightChild.addChild(child);
                }
            }
        }

        public int getX() {
            return x;
        }

        public int getY() {
            return y;
        }
    }
}

