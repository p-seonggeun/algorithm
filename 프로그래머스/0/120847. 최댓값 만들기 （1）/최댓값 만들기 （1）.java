import java.util.*;
class Solution {
    public int solution(int[] numbers) {
        int answer = 0;
        Arrays.sort(numbers);
        int index = numbers.length;
        answer = numbers[index - 1] * numbers[index - 2];
        return answer;
    }
}