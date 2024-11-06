import java.util.*;
class Solution {
    public int[] solution(int n) {
        Set<Integer> list = new HashSet<>();
        int number = 2;
        
        while (n > 1) {
            if (n % number == 0) {
                list.add(number);
                n = n / number;
            } else {
                number++;
            }
        }

        int[] answer = list.stream().mapToInt(Integer::intValue).toArray();
        Arrays.sort(answer);
        return answer;
    }
}