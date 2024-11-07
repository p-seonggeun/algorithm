import java.util.*;

class Solution {
    public long solution(String numbers) {
        HashMap<String, Integer> number = new HashMap<>(Map.of("zero", 0, "one", 1, "two", 2, "three", 3,
                "four", 4, "five", 5, "six", 6,
                "seven", 7, "eight", 8, "nine", 9));

        StringBuilder sb = new StringBuilder();
        StringBuilder temp = new StringBuilder();
        String[] split = numbers.split("");
        for (String s : split) {
            sb.append(s);
            if (number.containsKey(sb.toString())) {
                temp.append(number.get(sb.toString()));
                sb.setLength(0);
            }
        }

        long answer = Long.parseLong(temp.toString());
        return answer;
    }
}