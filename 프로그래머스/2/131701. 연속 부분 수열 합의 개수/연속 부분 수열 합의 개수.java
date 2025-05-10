import java.util.*;

class Solution {
    public int solution(int[] elements) {
        int answer = 0;
        HashSet<Integer> set = new HashSet<>();
        for (int length = 1; length <= elements.length; length++) { // 길이
            for (int i = 0; i < elements.length; i++) { // 기준점
                int start = i;
                int end = i + length;
                int temp = 0;
                for (int j = start; j < end; j++) {
                    int index = j % elements.length;
                    temp += elements[index];
                }
                set.add(temp);
            }
        }
        answer = set.size();
        return answer;
    }
}