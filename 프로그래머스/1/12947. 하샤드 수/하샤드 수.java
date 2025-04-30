class Solution {
    public boolean solution(int x) {
        String[] s = String.valueOf(x).split("");
        int t = 0;
        for (int i = 0; i < s.length; i++) {
            int temp = Integer.valueOf(s[i]);
            t += temp;
        }
        if (x % t == 0) {
            return true;
        }
        return false;
    }
}