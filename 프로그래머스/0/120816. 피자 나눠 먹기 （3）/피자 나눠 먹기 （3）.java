class Solution {
    public int solution(int slice, int n) {
        int answer = 0;
        if (slice >= n) {
            answer = 1;
        } else {
            answer = (n % slice != 0) ? (n / slice) + 1 : (n / slice);
        }
        return answer;
    }
}