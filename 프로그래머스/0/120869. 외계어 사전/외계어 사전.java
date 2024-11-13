class Solution {
    public int solution(String[] spell, String[] dic) {
        int answer = 0;
        
        for (String d : dic) {
            boolean isContain = true;
            for (String s : spell) {
                if (!d.contains(s)) {
                    isContain = false;
                }
            }
            if (isContain) {
                return 1;
            }
        }
        
        return 2;
    }
}