import java.util.*;

class Solution {
    public long[] solution(int x, int n) {
        long[] answer = {};
        List<Long> temp = new ArrayList<>();
        long l = x;
        for (int i = 0; i < n; i++) {
            temp.add(l);
            l += x;
        }
        
        answer = temp.stream()
            .mapToLong(t -> t)
            .toArray();
        
        return answer;
    }
}