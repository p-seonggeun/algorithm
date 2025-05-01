class Solution {
    public int solution(int n) {
        int answer = 0;
        int length = 0;
        for (char c : Integer.toBinaryString(n).toCharArray()) {
            if (c == '1') {
                length++;
            }
        }
        
        for (int i = n + 1; i < 1_000_000; i++) {
            int temp = 0;
            for (char c : Integer.toBinaryString(i).toCharArray()) {
                if (c == '1') {
                    temp++;
                }        
            }
            if (length == temp) {
                return i;
            }
        }
        return answer;
    }
}