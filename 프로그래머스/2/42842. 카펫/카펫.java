class Solution {
    public int[] solution(int brown, int yellow) {
        int[] answer = {};
        // 노란 가로 a 노란 세로 b
        // 갈색 가로 a + 2 갈색 세로 b + 2
        // 갈색 개수 = (a + 2) * (b + 2) - (a * b)
        // 노란 개수 = (a * b)
        int a = 0;
        int b = 0;
        for (int i = 1; i <= yellow; i++) {
            if (yellow % i == 0) {
                a = yellow / i;
                b = i;
                System.out.println(a + " " + b);
                
                if ((a + 2) * (b + 2) - (a * b) == brown) {
                    return new int[]{a + 2, b + 2};
                }
            }
        }
        return answer;
    }
}