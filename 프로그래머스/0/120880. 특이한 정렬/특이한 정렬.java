import java.util.*;

class Solution {
    public static int[] solution(int[] numlist, int n) {
        Integer[] num = Arrays.stream(numlist)
                .boxed()
                .toArray(Integer[]::new);

        Arrays.sort(num, new Custom(n));
        return Arrays.stream(num).mapToInt(i -> i).toArray();
    }
    
    static class Custom implements Comparator<Integer> {

        private final int n;

        public Custom(int n) {
            this.n = n;
        }

        @Override
        public int compare(Integer o1, Integer o2) {
            if (Math.abs(o1 - n) != Math.abs(o2 - n)) {
                return Integer.compare(Math.abs(o1 - n), Math.abs(o2 - n));
            } else {
                return Integer.compare(o1, o2) * -1;
            }
        }
    }
}