class Solution {
    public int solution(int order) {
        int answer = 0;
        String str = order + "";
        String[] arr = str.split("");
        
        for (String s : arr) {
            if (s.equals("3") || s.equals("6") || s.equals("9")) {
                answer++;
            }
        }

        return answer;
    }
}