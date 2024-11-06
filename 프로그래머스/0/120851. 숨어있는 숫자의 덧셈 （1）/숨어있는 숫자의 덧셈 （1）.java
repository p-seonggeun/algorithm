class Solution {
    public int solution(String my_string) {
        int answer = 0;
        
        for (int i = 0; i < my_string.length(); i++) {
            if (Character.isDigit(my_string.charAt(i))) {
                String s = String.valueOf(my_string.charAt(i));
                answer += Integer.parseInt(s);
            }
        }
        
        return answer;
    }
}