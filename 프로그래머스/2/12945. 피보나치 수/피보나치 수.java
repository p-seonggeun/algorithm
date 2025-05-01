class Solution {
    public int solution(int n) {
        
        long[] temp = new long[100001];
        temp[1] = 1;
        for (int i = 2; i < temp.length; i++) {
            temp[i] = (temp[i - 1] + temp[i - 2]) % 1234567;
        }
        
        return (int) temp[n];
    }
}