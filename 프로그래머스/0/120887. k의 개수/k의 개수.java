class Solution {
    public static int solution(int i, int j, int k) {
        String b = String.valueOf(k);
        int answer = 0;

        for (int a = i; a <= j; a++) {
            String s = String.valueOf(a);
            answer += s.length() - s.replace(b, "").length();
        }

        return answer;
    }
}