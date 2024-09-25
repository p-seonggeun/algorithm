class Solution {
    public int solution(int num1, int num2) {
        int answer = 0;
        double a = (double) num1;
        double b = (double) num2;
        answer = (int) ((a / b) * 1000);
        return answer;
    }
}