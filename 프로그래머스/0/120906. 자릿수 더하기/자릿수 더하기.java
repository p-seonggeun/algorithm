class Solution {
    public int solution(int n) {
        String s = n + "";
        String[] split = s.split("");
        int answer = 0;

        for (String string : split) {
            answer += Integer.parseInt(string);
        }
        
        return answer;
    }
}