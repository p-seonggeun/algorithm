import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        String[] split = scanner.nextLine().split(" ");
        int total = Integer.parseInt(split[0]);
        int jump = Integer.parseInt(split[1]);
        boolean[] table = new boolean[total];
        Arrays.fill(table, true);

        List<Integer> list = new ArrayList<>();
        int index = -1;
        int move = jump;
        while (list.size() != total) {

            while (move > 0) {
                if (table[++index % total]) {
                    move--;
                }
            }
            move = jump;
            table[index % total] = false;
            list.add(index % total + 1);
        }

        printAnswer(list);
    }

    private static void printAnswer(List<Integer> list) {
        System.out.print("<");
        for (int i = 0; i < list.size(); i++) {
            System.out.print(list.get(i));
            if (i < list.size() - 1) {
                System.out.print(", ");
            }
        }
        System.out.println(">");
    }
}