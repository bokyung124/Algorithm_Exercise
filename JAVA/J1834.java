import java.util.Scanner;

public class J1834 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long n = sc.nextInt();

        long sum = (n - 1) * (n + 1 + (n + 1) * (n - 1)) / 2;

        System.out.println(sum);
    }
}
