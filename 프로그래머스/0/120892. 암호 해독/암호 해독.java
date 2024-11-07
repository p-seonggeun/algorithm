class Solution {
    public String solution(String cipher, int code) {
        StringBuilder sb = new StringBuilder();
        int count = 0;
        
        for (int i = 0; i < cipher.length(); i++) {
            if (++count == code) {
                count = 0;
                sb.append(cipher.charAt(i));
            }
        }

        String answer = sb.toString();
        return answer;
    }
}