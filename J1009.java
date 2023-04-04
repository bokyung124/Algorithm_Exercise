import java.util.*;

public class J1009 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int num = Integer.parseInt(sc.next());
        int a, b, r;

        for (int i = 0; i < num; i++) {
            a = sc.nextInt();
            b = sc.nextInt();
            r = 1;
            for (int j = 0; j < b; j++) {
                r = a * r % 10;
            }
            if (r == 0) r = 10;
            System.out.println(r);
        }
    }
}