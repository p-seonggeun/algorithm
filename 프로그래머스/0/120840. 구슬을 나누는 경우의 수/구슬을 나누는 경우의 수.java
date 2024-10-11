import java.math.*;

class Solution {
    public BigInteger f(int number) {
        BigInteger b = new BigInteger("1");
        for (int i = number; i > 0; i--) {
            b = b.multiply(BigInteger.valueOf(i));
        }
        return b;
    }
    
    public int solution(int balls, int share) {
        BigInteger a = f(balls);
        BigInteger b = f(share).multiply(f(balls - share));
        
        BigInteger result = a.divide(b);
        
        return result.intValue();
    }
}
