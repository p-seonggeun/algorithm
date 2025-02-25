class Solution {
    public static String solution(String bin1, String bin2) {
        int int1 = toDecimalBy(bin1);
        int int2 = toDecimalBy(bin2);
        return toBinaryBy(int1 + int2);
    }

    private static int toDecimalBy(String input) {
        int result = 0;
        int length = input.length();

        for (int i = 0; i < length; i++) {
            int pow = (int) Math.pow(2, length - i - 1);
            result += pow * Integer.parseInt(input.substring(i, i + 1));
        }

        return result;
    }

    private static String toBinaryBy(int input) {
        StringBuilder result = new StringBuilder();

        do {
            result.append(input % 2);
            input = input / 2;
        } while (input >= 1);
        return result.reverse().toString();
    }
}