import java.util.ArrayList;
import java.util.List;

class Solution {
    public int[] solution(int[] numbers) {
        List<Integer> answer = new ArrayList<>();
        
        for (int number : numbers) {
            answer.add(number * 2);
        }
        
        return answer.stream()
                     .mapToInt(i -> i)
                     .toArray();
    }
}