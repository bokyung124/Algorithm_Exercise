import java.util.*;

public class J1292 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int start = sc.nextInt();
        int end = sc.nextInt();
        ArrayList<Integer> array = new ArrayList<>();
        int cnt = 1;
        int sum = 0;

        for (int i = 0; i < end; i++) {
            for (int j = 0; j < cnt; j++) {
                array.add(cnt);
            }
            cnt++;
        }

        for (int i = start; i <= end; i++) {
            sum += array.get(i-1);
        }

        System.out.println(sum);
    }
}
