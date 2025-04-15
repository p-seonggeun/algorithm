import java.util.*;
import java.lang.*;

class Solution {
    public String solution(String s) {
        StringBuilder sb = new StringBuilder();
        
        String[] l = s.split(" ");
        int ma = Integer.parseInt(l[0]);
        int mi = Integer.parseInt(l[0]);
        
        for (int i = 1; i < l.length; i++) {
            ma = Math.max(ma, Integer.parseInt(l[i]));
            mi = Math.min(mi, Integer.parseInt(l[i]));
        }
        
        sb.append(mi);
        sb.append(" ");
        sb.append(ma);
        
        String answer = sb.toString();
        return answer;
    }
}