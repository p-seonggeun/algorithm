import java.util.*;

class Solution {
    public int solution(int[] A, int[] B) {
        int answer = 0;
        
//         Integer[] tA = Arrays.stream(A)
//             .boxed()
//             .toArray(Integer[]::new);
        
//         Integer[] tB = Arrays.stream(B)
//             .boxed()
//             .toArray(Integer[]::new);
        
//         Arrays.sort(tA);
//         Arrays.sort(tB, Collections.reverseOrder());
        
        Arrays.sort(A);
        Arrays.sort(B);
        
        for (int i = 0; i < A.length; i++) {
            answer += A[i] * B[B.length - (i + 1)];
        }
        return answer;
    }
}