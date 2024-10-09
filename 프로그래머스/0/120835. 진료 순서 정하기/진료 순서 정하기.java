import java.util.*;
class Solution {
    public int[] solution(int[] emergency) {
        int[] answer = {};
        List<Integer> b = new ArrayList<>();
        HashMap<Integer, Integer> h = new HashMap<>();
        Integer[] a = Arrays.stream(emergency).boxed().toArray(Integer[]::new);
        
        Arrays.sort(a, Comparator.reverseOrder());
        
        for (int i = 0; i < a.length; i++) {
            System.out.println(i + 1 + " " + a[i]);
            h.put(a[i], i + 1);
        }
        
        for (int i : emergency) {
            b.add(h.get(i));
        }
        
        answer = b.stream().mapToInt(c -> c).toArray();
        
        return answer;
    }
}