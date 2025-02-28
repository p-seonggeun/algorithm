class Solution {
    public static int solution(String A, String B) {
        StringBuilder sb = new StringBuilder();
        sb.append(A);
        int answer = 0;
        while (!sb.toString().equals(B)) {
            if (answer > A.length() + 1) {
                return -1;
            }
            sb.insert(0, sb.charAt(A.length() - 1));
            sb.deleteCharAt(A.length());
            answer++;
        }

        return answer;
    }
}