import java.util.*;

class Solution {
    public static int solution(int[] nums) {
        List<Integer> list = new ArrayList<>();
        for (int num : nums) {
            if (!list.contains(num)) {
                list.add(num);
            }
        }

        if (list.size() > (nums.length / 2)) {
            return nums.length / 2;
        }
        return list.size();
    }
}