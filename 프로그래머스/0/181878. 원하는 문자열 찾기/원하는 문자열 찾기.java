class Solution {
    public int solution(String myString, String pat) {
        int answer = 0;
        if (myString.length() < pat.length()) {
            return answer;
        }
        if (myString.toLowerCase().contains(pat.toLowerCase())) {
            return 1;
        }
        return answer;
    }
}