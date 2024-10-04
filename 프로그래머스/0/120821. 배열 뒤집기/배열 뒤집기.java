import java.util.*;
class Solution {
    public int[] solution(int[] num_list) {
        List<Integer> a = new ArrayList<>();
        
        for (int i = num_list.length - 1; i >= 0; i--) {
            a.add((Integer) num_list[i]);
        }
        
        int[] answer = a.stream().mapToInt(num -> num).toArray();
        
        return answer;
    }
}