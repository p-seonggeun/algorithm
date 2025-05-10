import java.util.*;

class Solution {
    public int solution(int k, int[] tangerine) {
        int answer = 0;
        HashMap<Integer, Integer> map = new HashMap<>();
        
        for (int i : tangerine) {
            map.put(i, map.getOrDefault(i, 0) + 1);
        }
        
        List<Integer> list = new ArrayList(Arrays.asList(map.values().toArray()));
        list.sort(Collections.reverseOrder());
        
        for (int i : list) {
            if (k <= 0) {
                return answer;
            }
            
            k -= i;
            answer++;
        }
        
        return answer;
    }
}