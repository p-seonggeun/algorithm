class Solution {
        public static int solution(int[][] dots) {
            double gradient1 = ((double) (dots[0][1] - dots[1][1])) / (dots[0][0] - dots[1][0]);
            double gradient2 = ((double) (dots[2][1] - dots[3][1])) / (dots[2][0] - dots[3][0]); 
            if (gradient1 == gradient2) {
                return 1;
            }
            
            double gradient3 = ((double) (dots[0][1] - dots[2][1])) / (dots[0][0] - dots[2][0]);
            double gradient4 = ((double) (dots[1][1] - dots[3][1])) / (dots[1][0] - dots[3][0]);
            if (gradient3 == gradient4) {
                return 1;
            }

            double gradient5 = ((double) (dots[0][1] - dots[3][1])) / (dots[0][0] - dots[3][0]);
            double gradient6 = ((double) (dots[1][1] - dots[2][1])) / (dots[1][0] - dots[2][0]);
            if (gradient5 == gradient6) {
                return 1;
            }

            return 0;
        }
    }