import java.util.*;

class Solution {
    public static int solution(int n, int[][] costs) {
        int[] parent = new int[n];
        List<Edge> edges = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            parent[i] = i;
        }

        for (int[] cost : costs) {
            edges.add(new Edge(cost[2], cost[0], cost[1]));
        }

        Collections.sort(edges);

        int result = 0;
        for (Edge edge : edges) {
            int distance = edge.getDistance();
            int nodeA = edge.getNodeA();
            int nodeB = edge.getNodeB();

            if (find_parent(parent, nodeA) == find_parent(parent, nodeB)) {
                continue;
            }

            union_parent(parent, nodeA, nodeB);
            result += distance;
        }

        return result;
    }

    public static int find_parent(int[] parent, int x) {
        if (parent[x] != x) {
            parent[x] = find_parent(parent, parent[x]);
        }
        return parent[x];
    }

    public static void union_parent(int[] parent, int a, int b) {
        a = find_parent(parent, a);
        b = find_parent(parent, b);

        if (a < b) {
            parent[b] = a;
        } else {
            parent[a] = b;
        }
    }
    

    static class Edge implements Comparable<Edge> {

        private int distance;
        private int nodeA;
        private int nodeB;

        public Edge(int distance, int nodeA, int nodeB) {
            this.distance = distance;
            this.nodeA = nodeA;
            this.nodeB = nodeB;
        }

        public int getDistance() {
            return distance;
        }

        public int getNodeA() {
            return nodeA;
        }

        public int getNodeB() {
            return nodeB;
        }

        @Override
        public int compareTo(Edge o) {
            if (this.distance < o.distance) {
                return -1;
            }
            return 1;
        }
    }
}
