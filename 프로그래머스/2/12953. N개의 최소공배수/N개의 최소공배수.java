import java.util.*;
import java.lang.Math;

class Solution {
    public int solution(int[] arr) {
        Integer[] temp = Arrays.stream(arr)
            .boxed()
            .toArray(Integer[]::new);
        Arrays.sort(temp, Collections.reverseOrder());
        
        int answer = temp[0];
        for (int i = 1; i < arr.length; i++) {
            answer = Math.max(answer, lcm(answer, temp[i]));
        }
        
        return answer;
    }
    
    public int gcd(int a, int b) {
        if (b == 0) {
            return a;
        }
        return gcd(b, a % b);
    }
    
    public int lcm(int a, int b) {
        return (a * b) / gcd(a, b);
    }
}