import java.util.*;

class Solution {
    public int solution(int n) {
        int answer = 0;
        Set<Integer> set = new HashSet<>();
        for (int i = 1; i <= n; i++) {
            if (set.contains(i)) {
                break;
            }
            if (n % i == 0) {
                set.add(i);
            }
        }
        
        answer = set.stream()
            .mapToInt(s -> s)
            .sum();
        
        return answer;
    }
}