import java.util.*;

class Solution {
    public int solution(int[] array) {
        int answer = 0;
        int[] index = new int[1001];
        int[] count = { 0 };
        
        for (int arr : array) {
            index[arr]++;
        }
        
        int mode = Arrays.stream(index).max().getAsInt();      
        
        Arrays.stream(index)
            .forEach(i -> {
                if (i == mode) {
                    count[0]++;
                }
            });
        
        if (count[0] == 1) {
            for (int i = 0; i < index.length; i++) {
                if (index[i] == mode) {
                    answer = i;
                    break;
                }
            }
        } else if (count[0] >= 2) {
            answer = -1;
        }
        
        
        return answer;
    }
}