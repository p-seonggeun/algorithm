class Solution {
    public int solution(int[] numbers, int k) {
        int answer = 0;
        int count = 1;
        int temp = 0;
        
        while (count < k) {
            count++;
            temp += 2;
            if (temp >= numbers.length) {
                temp = temp % numbers.length;
            }
        }
        answer = numbers[temp];
        return answer;
    }
}