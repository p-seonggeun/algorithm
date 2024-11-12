class Solution {
    public int solution(String my_string) {
        StringBuilder sb = new StringBuilder();
        int answer = 0;

        char[] charArray = my_string.toCharArray();
        for (char c : charArray) {
            if (Character.isDigit(c)) {
                sb.append(c);
            } else {
                if (sb.length() != 0) {
                    answer += Integer.parseInt(sb.toString());
                }
                sb.setLength(0);
            }
        }
        
        if (sb.length() != 0) {
            answer += Integer.parseInt(sb.toString());
        }
        
        return answer;
    }
}