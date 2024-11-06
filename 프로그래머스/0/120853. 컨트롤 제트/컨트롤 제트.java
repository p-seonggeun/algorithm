import java.util.*;

class Solution {
    public int solution(String s) {
        List<Integer> answer = new ArrayList<>();
        String[] strings = s.split(" ");
        
        for (String string : strings) {
            if (!string.equals("Z")) {
                answer.add(Integer.valueOf(string));
            } else {
                answer.remove(answer.size() - 1);
            }
        }

        int ans = 0;
        for (Integer i : answer) {
            ans += i;
        }
        
        return ans;
    }
}