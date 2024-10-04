class Solution {
    public int solution(int price) {
        int answer = 0;
        double discount = 0;
        if (price >= 500_000) discount = 0.8;
        else if (price >= 300_000) discount = 0.9;
        else if (price >= 100_000) discount = 0.95;
        else discount = 1;
        
        answer = (int) (price * discount);
        
        return answer;
    }
}