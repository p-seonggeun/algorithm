class Solution {
    public int solution(String number) {
        int answer = 0;
        String[] numbers = number.split("");
        for (String num : numbers) {
            answer += Integer.valueOf(num);
        }
        return answer % 9;
    }
}