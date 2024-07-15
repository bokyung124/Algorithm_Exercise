import java.util.*;
public class J1076 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Map<String, String> add = new HashMap<>();
        Map<String, String> mul = new HashMap<>();

        add.put("black", "0");
        add.put("brown", "1");
        add.put("red", "2");
        add.put("orange", "3");
        add.put("yellow", "4");
        add.put("green", "5");
        add.put("blue", "6");
        add.put("violet", "7");
        add.put("grey", "8");
        add.put("white", "9");

        mul.put("black", "1");
        mul.put("brown", "10");
        mul.put("red", "100");
        mul.put("orange", "1000");
        mul.put("yellow", "10000");
        mul.put("green", "100000");
        mul.put("blue", "1000000");
        mul.put("violet", "10000000");
        mul.put("grey", "100000000");
        mul.put("white", "1000000000");

        String a = sc.nextLine();
        String b = sc.nextLine();
        String m = sc.nextLine();

        String add_first = add.get(a) + add.get(b);
        String multi = mul.get(m);
        String ans = add_first + multi.substring(1);
        long answer = Long.parseLong(ans);

        System.out.println(answer);
    }
}
