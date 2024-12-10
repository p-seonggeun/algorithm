import java.util.*;

class Solution {
    public static int[] solution(int[] progresses, int[] speeds) {
            List<Integer> temp = new ArrayList<>(); // 정답을 담아놓을 임시 리스트
            ArrayDeque<Integer> queue = new ArrayDeque<>(); // 작업 담아놓을 큐
            ArrayDeque<Integer> speedQueue = new ArrayDeque<>(); // 작업 속도 담아놓을 큐
            // 큐에 작업 담기
            for (int progress : progresses) {
                queue.addLast(progress);
            }

            for (int speed : speeds) {
                speedQueue.addLast(speed);
            }

            Integer progress = queue.pollFirst();
            Integer speed = speedQueue.pollFirst();
            int days = (int) Math.ceil((double) (100 - progress) / speed); // 작업이 완료될 때 까지 소요되는 날
            int count = 1;

            while (!queue.isEmpty()) { // 큐가 비어있지 않으면(큐가 빌 때까지) 반복
                Integer nextProgress = queue.pollFirst();
                Integer nextSpeed = speedQueue.pollFirst();
                int nextDays = (int) Math.ceil((double) (100 - nextProgress) / nextSpeed); // 작업이 완료될 때 까지 소요되는 날

                if (days >= nextDays) { // 다음 작업보다 앞의 작업이 소요되는 날이 더 큰 경우
                    count++;
                } else { // 다음 작업이 더 오래걸리는 경우
                    days = nextDays;
                    temp.add(count);
                    count = 1;
                }
            }
            temp.add(count); // 반복문이 종료 될 경우 count에 남아있는 작업들을 넣어줘야 함

            int[] answer = temp.stream().mapToInt(Integer::intValue).toArray();
            return answer;
        }
}