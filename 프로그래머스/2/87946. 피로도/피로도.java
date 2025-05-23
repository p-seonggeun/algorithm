import java.lang.Math;

class Solution {
    public int solution(int k, int[][] dungeons) {
        boolean[] visited = new boolean[dungeons.length];
        int answer = dfs(0, dungeons, visited, k);
        return answer;
    }
    
    public int dfs(int count, int[][] dungeons, boolean[] visited, int k) {
        int max = count;
        
        for (int i = 0; i < dungeons.length; i++) {
            if (!visited[i] && dungeons[i][0] <= k) {
                visited[i] = true;
                max = Math.max(max, dfs(count + 1, dungeons, visited, k - dungeons[i][1]));
                visited[i] = false;
            }
        }
        
        return max;
    }
}