import java.util.*;

public class J1032 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int cnt = Integer.parseInt(sc.nextLine());
        String[] array;
        String[] array_next;

        String str = sc.nextLine();
        array = str.split("");
        int n = array.length;

        for (int i = 0; i < cnt-1; i++) {
            String next = sc.nextLine();
            array_next = next.split("");
            for (int j = 0; j < n; j++) {
                if (array[j].equals(array_next[j])) {
                    continue;
                } else if (array[j] != array_next[j]) {
                    array[j] = "?";
                }
            }
        }

        for (int i = 0; i < n; i++) {
            System.out.print(array[i]);
        }
    }
}
