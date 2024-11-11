class Solution {
    public int solution(int[] array) {
        int answer = 0;
        
        for (int i : array) {
            String s = String.valueOf(i);
            char[] charArray = s.toCharArray();
            for (char c : charArray) {
                if (c == '7') {
                    answer++;
                }
            }
        }
        return answer;
    }
}