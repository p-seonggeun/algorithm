import java.util.*;

class Solution {
    public static int[] solution(String[] enroll, String[] referral, String[] seller, int[] amount) {

        Map<String, Person> map = new HashMap<>();
        map.put("-", new Person("-", null));
        for (int i = 0; i < enroll.length; i++) {
            map.put(enroll[i], new Person(enroll[i], map.get(referral[i])));
        }

        for (int i = 0; i < seller.length; i++) {
            String name = seller[i];
            int sellMoney = amount[i] * 100;

            while (map.get(name).getInviter() != null && divide(sellMoney)) {
                Person person = map.get(name);
                sellMoney = person.plusMoney(sellMoney);

                name = person.getInviter().getName();
            }

            map.get(name).plusMoney(sellMoney);
        }

        List<Integer> list = new ArrayList<>();
        for (int i = 0; i < enroll.length; i++) {
            list.add(map.get(enroll[i]).getMoney());
        }
        int[] answer = list.stream().mapToInt(Integer::intValue).toArray();

        return answer;
    }

    public static boolean divide(int money) {
        if ((int)(money * 0.1) <= 0) {
            return false;
        }
        return true;
    }

    static class Person {
        private final String name;
        private final Person inviter;
        private int money;

        public Person(String name, Person inviter) {
            this.name = name;
            this.inviter = inviter;
        }

        public int plusMoney(int money) {
            if (this.inviter == null) {
                this.money += money;
                return 0;
            }

            int balance = (int) (money * 0.1);
            this.money += money - balance;
            return balance;
        }

        public String getName() {
            return name;
        }

        public Person getInviter() {
            return inviter;
        }

        public int getMoney() {
            return money;
        }

        @Override
        public String toString() {
            return "Person{" +
                    "name='" + name + '\'' +
                    ", money=" + money +
                    '}';
        }
    }
}