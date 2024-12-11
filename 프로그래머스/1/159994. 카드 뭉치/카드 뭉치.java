import java.util.*;

class Solution {
    public static String solution(String[] cards1, String[] cards2, String[] goal) {
        StringBuilder sb = new StringBuilder();
        ArrayDeque<String> card1 = new ArrayDeque<>();
        ArrayDeque<String> card2 = new ArrayDeque<>();

        Collections.addAll(card1, cards1); // card1에 카드 다 넣기
        Collections.addAll(card2, cards2); // card2에 카드 다 넣기

        for (String s : goal) {
            if (!card1.isEmpty() && card1.peekFirst().equals(s)) {
                sb.append(card1.pollFirst());
                continue;
            }
            if (!card2.isEmpty() && card2.peekFirst().equals(s)) {
                sb.append(card2.pollFirst());
                continue;
            }
            return "No";
        }
        return "Yes";
    }
}