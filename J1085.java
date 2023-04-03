import java.util.Scanner;

public class J1085 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int x = sc.nextInt();
        int y = sc.nextInt();
        int w = sc.nextInt();
        int h = sc.nextInt();

        int left = x;
        int right = w-x;
        int up = h-y;
        int down = y;

        int[] arr = {left, right, up, down};
        int min = arr[0];
        for(int num : arr) {
            if(num < min) {
                min = num;
            }
        }
        System.out.print(min);
    }
}
