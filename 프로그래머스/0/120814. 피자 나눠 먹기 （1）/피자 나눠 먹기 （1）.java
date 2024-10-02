class Solution {
    public int solution(int n) {
        int answer = 0;
        boolean rest = (n % 7 != 0) ? true : false;
        answer = (int) n / 7;
        
        if (rest) {
            answer++;
        }
        
        return answer;
    }
}