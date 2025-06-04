class Solution {
    public String solution(String code) {
        StringBuilder sb = new StringBuilder();
        int mode = 0;
        String[] codeArr = code.split("");
        for (int i = 0; i < codeArr.length; i++) {
            if (mode == 0) {
                if (codeArr[i].equals("1")) {
                    mode = 1;
                } else {
                    if (i % 2 == 0) {
                        sb.append(codeArr[i]);
                    }
                }
            } else {
                if (codeArr[i].equals("1")) {
                    mode = 0;
                } else {
                    if (i % 2 != 0) {
                        sb.append(codeArr[i]);
                    }
                }
            }
        }
        String answer = sb.toString();
        if (answer.length() == 0) {
            return "EMPTY";
        }
        return answer;
    }
}