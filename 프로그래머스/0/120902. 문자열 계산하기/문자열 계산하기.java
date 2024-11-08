class Solution {
    public int solution(String my_string) {
        int answer = 0;
        boolean plus = true;

        String[] split = my_string.split(" ");
        for (String s : split) {
            if (Character.isDigit(s.charAt(0))) {
                if (plus) {
                    answer += Integer.parseInt(s);
                } else {
                    answer -= Integer.parseInt(s);
                }
            } else {
                if (s.equals("+")) {
                    plus = true;
                } else {
                    plus = false;
                }
            }
        }

        return answer;
    }
}