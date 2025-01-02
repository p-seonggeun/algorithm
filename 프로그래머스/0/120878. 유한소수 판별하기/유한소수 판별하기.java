class Solution {
    public static int solution(int a, int b) {
        int gcd = 0;
        if (a >= b) {
            gcd = gcd(a, b);
        } else {
            gcd = gcd(b, a);
        }

        b = b / gcd;
        int count = 0;
        while (b != 1) {
            if (b % 2 == 0) {
                b /= 2;
                count = 0;
            }
            if (b % 5 == 0) {
                b /= 5;
                count = 0;
            }
            count++;

            if (count >= 2) {
                return 2;
            }
        }
        return 1;
    }

    public static int gcd(int a, int b) {
    if (b == 0) {
        return a;
    }
    return gcd(b, a % b);
    }
}

