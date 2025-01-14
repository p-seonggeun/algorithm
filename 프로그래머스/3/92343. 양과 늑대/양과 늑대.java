import java.util.*;

class Solution {
    public static int solution(int[] info, int[][] edges) {
        int[] answer = {0, 0};
        int[] count = {1, 0}; // 양, 늑대 개수
        List<Node> list = new ArrayList<>();

        for (int i = 0; i < info.length; i++) {
            list.add(new Node(i, info[i]));
        }

        for (int[] edge : edges) {
            int parent = edge[0];
            int child = edge[1];

            Node parentNode = list.get(parent);
            Node childNode = list.get(child);
            parentNode.addMoves(childNode);
        }


        Node currentNode = list.get(0);
        List<Node> canMoveNodes = currentNode.getNodes();
        dfs(currentNode, canMoveNodes, list, count, answer);

        return answer[0];
    }
    
    /**
     * @param nodes 이동할 수 있는 노드 리스트
     * @param list  연결되어 있는 전체 리스트
     */
    public static void dfs(Node currentNode, List<Node> nodes, List<Node> list, int[] count, int[] answer) {
        if ((count[0] <= count[1]) || (nodes.isEmpty())) {
            if (count[0] > answer[0]) {
                answer[0] = count[0];
            }
            return;
        }

        for (int i = 0; i < nodes.size(); i++) {
            Node targetNode = nodes.get(i);
            List<Node> targetNodeCanMove = targetNode.getNodes();

            nodes.remove(targetNode);
            count[targetNode.getAnimal()]++;
            nodes.addAll(targetNodeCanMove);

            dfs(targetNode, nodes, list, count, answer);

            nodes.removeAll(targetNodeCanMove);
            count[targetNode.getAnimal()]--;
            nodes.add(i, targetNode);
        }
    }

}

class Node {
    private final int number; // 내 번호
    private final int animal; // 0이면 양, 1이면 늑대
    private List<Node> nodes = new ArrayList<>(); // 갈 수 있는 노드

    public Node(int number, int animal) {
        this.number = number;
        this.animal = animal;
    }

    public void addMoves(Node node) {
        this.nodes.add(node);
    }

    public int getNumber() {
        return number;
    }

    public int getAnimal() {
        return animal;
    }

    public List<Node> getNodes() {
        return nodes;
    }

    @Override
    public String toString() {
        return "Node{" +
                "number=" + number +
                ", animal=" + animal +
                ", moves=" + canMoveNode(nodes) +
                '}';
    }

    public List<Integer> canMoveNode(List<Node> nodes) {
        List<Integer> result = new ArrayList<>();
        for (Node node : nodes) {
            result.add(node.getNumber());
        }

        return result;
    }
}