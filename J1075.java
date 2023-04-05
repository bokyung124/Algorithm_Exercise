import java.util.*;

public class J1075 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int test;
        int n = Integer.parseInt(sc.nextLine());
        int f = Integer.parseInt(sc.nextLine());
        String sn = Integer.toString(n);
        String ch = sn.substring(sn.length() - 2);
        String first = sn.substring(0, sn.length() - 2);
        test = Integer.parseInt(first+"00");

        while (true) {
            if (test % f == 0) {
                String ans = Integer.toString(test);
                int prt = Integer.parseInt(ans.substring(ans.length()-2));
                System.out.printf("%02d", prt);
                break;
            }
            test += 1;
        }
    }
}
