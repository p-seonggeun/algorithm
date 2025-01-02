class Solution {
    public static int solution(int[][] lines) {
        int[] l = new int[201];
        int answer = 0;

        for (int[] line : lines) {
            for (int i = line[0]; i < line[1]; i++) {
                l[i + 100] += 1;
            }
        }

        for (int i = 0; i < 201; i++) {
            if (l[i] >= 2) {
                answer++;
            }
        }
        return answer;
    }
}