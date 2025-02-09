import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] split = br.readLine().split(" ");
        int N = Integer.parseInt(split[0]);
        int M = Integer.parseInt(split[1]);
        int[] parent = new int[N + 1];

        for (int i = 1; i <= N; i++) {
            parent[i] = i;
        }

        List<Edge> edges = new ArrayList<>();
        for (int i = 0; i < M; i++) {
            String[] info = br.readLine().split(" ");
            Edge edge = new Edge(Integer.parseInt(info[0]), Integer.parseInt(info[1]), Integer.parseInt(info[2]));
            edges.add(edge);
        }
        Collections.sort(edges);

        int result = 0;
        List<Integer> distances = new ArrayList<>();
        for (int i = 0; i < M; i++) {
            
            Edge edge = edges.get(i);
            int nodeA = edge.getNodeA();
            int nodeB = edge.getNodeB();
            int distance = edge.getDistance();

            if (findParent(parent, nodeA) == findParent(parent, nodeB)) {
                continue;
            }

            unionParent(parent, nodeA, nodeB);
            result += distance;
            distances.add(distance);
        }

        System.out.println(result - distances.get(distances.size() - 1));

    }

    public static int findParent(int[] parent, int x) {
        if (parent[x] != x) {
            parent[x] = findParent(parent, parent[x]);
        }
        return parent[x];
    }

    public static void unionParent(int[] parent, int a, int b) {
        a = findParent(parent, a);
        b = findParent(parent, b);

        if (a < b) {
            parent[b] = a;
        } else {
            parent[a] = b;
        }
    }

    static class Edge implements Comparable<Edge> {

        private int nodeA;
        private int nodeB;
        private int distance;

        public Edge(int nodeA, int nodeB, int distance) {
            this.nodeA = nodeA;
            this.nodeB = nodeB;
            this.distance = distance;
        }

        @Override
        public int compareTo(Edge o) {
            return Integer.compare(distance, o.distance);
        }

        public int getNodeA() {
            return nodeA;
        }

        public int getNodeB() {
            return nodeB;
        }

        public int getDistance() {
            return distance;
        }
    }
}
