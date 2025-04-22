class Solution {
    boolean solution(String s) {
        boolean answer = true;
        int p = 0;
        int y = 0;
        
        String[] temp = s.split("");
        for (int i = 0; i < temp.length; i++) {
            if (String.valueOf(temp[i]).equals("p") || String.valueOf(temp[i]).equals("P")) {
                p++;
            }
            if (String.valueOf(temp[i]).equals("y") || String.valueOf(temp[i]).equals("Y")) {
                y++;
            }
        }
        
        if (p == y) {
            return true;
        }

        return false;
    }
}