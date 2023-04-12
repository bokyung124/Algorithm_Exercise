import java.util.*;

public class J2163 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int m = sc.nextInt();
        int cnt;

        if (n >= m) {
            cnt = (n-1) + (m-1)*n;
            System.out.println(cnt);
        }

        else if (n < m) {
            cnt = (m-1) + (n-1)*m;
            System.out.println(cnt);
        }
    }
}
