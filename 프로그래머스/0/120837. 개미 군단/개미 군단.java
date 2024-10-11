class Solution {
    public int solution(int hp) {
        int answer = 0;
        if (hp >= 5) {
            answer += hp / 5;
            hp %= 5;
        }
        if (hp >= 3) {
            answer += hp / 3;
            hp %= 3;
        }
        if (hp >= 1) {
            answer += hp / 1;
            hp %= 1;
        }
        return answer;
    }
}