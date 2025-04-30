class Solution {
    public int solution(int[] numbers) {
        int answer = 0;
        for (int i = 0; i < 10; i++) {
            boolean flag = true;
            for (int j = 0; j < numbers.length; j++) {
                if (i == numbers[j]) {
                    flag = false;
                    break;
                }
            }
            if (flag == true) {
                answer += i;
            }
        }
        return answer;
    }
}