class Solution {
    public String solution(String my_string) {
        char[] charArray = my_string.toCharArray();
        StringBuilder sb = new StringBuilder();

        for (char c : charArray) {
            if (Character.isLowerCase(c)) {
                sb.append(Character.toUpperCase(c));
            } else {
                sb.append(Character.toLowerCase(c));
            }
        }

        String answer = sb.toString();
        return answer;
    }
}