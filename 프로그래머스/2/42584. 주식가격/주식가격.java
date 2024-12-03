import java.util.*;

class Solution {
public int[] solution(int[] prices) {
        int[] answer = new int[prices.length];
        int last_index = prices.length - 1;
        ArrayDeque<Integer[]> stack = new ArrayDeque<>();
        
        for (int i = 0; i < prices.length; i++) {
            while (!stack.isEmpty() && stack.peekLast()[1] > prices[i]) {
                Integer[] pop = stack.pollLast();
                answer[pop[0]] = i - pop[0];
            }
            stack.addLast(new Integer[]{i, prices[i]});
        }

        while (!stack.isEmpty()) {
            Integer[] pop = stack.pollLast();
            answer[pop[0]] = last_index - pop[0];
        }

        return answer;
    }
}