import java.util.*;

public class J1259 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        while(true) {
            String num = sc.nextLine();
            boolean flag = true;
            if(num.equals("0")) break;
            else {
                for (int i = 0; i < num.length()/2; i++) {
                        if (num.charAt(i) != num.charAt(num.length() - (i+1))) {
                            flag = false;
                            break;
                        }
                }
            }

            if(flag)
                System.out.println("yes");
            else
                System.out.println("no");
        }
        sc.close();
    }
}
