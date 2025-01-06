class Solution {
    public static int solution(int n, int a, int b) {
        int target1 = a - 1;
        int target2 = b - 1;

        if (big(a, b)) {
            target1 = b - 1;
            target2 = a - 1;
        }
        int answer = 1;

        while (true) {
            if (target1 + 1 == target2) {
                if (target1 / 2 == target2 / 2) {
                    break;
                }
            }
            target1 = target1 / 2;
            target2 = target2 / 2;
            answer++;
        }

        return answer;
    }

    public static boolean big(int a, int b) {
        if (a > b) {
            return true;
        }
        return false;
    }
}