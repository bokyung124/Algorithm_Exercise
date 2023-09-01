import java.util.*;

public class J1100 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        ArrayList<String> ls = new ArrayList<>();
        int piece = 0;

        for (int i = 0; i < 8; i++) {
            ls.add(sc.nextLine());
        }

        for (int i = 0; i < 8; i++) {

            // 홀수줄 -> 홀수번째가 흰색
            if (i % 2 == 0) {
                for (int j = 0; j < 8; j++) {
                    if (j % 2 == 0) {
                        if (ls.get(i).charAt(j) == 'F') {
                            piece++;
                        }
                    }
                }
            }

            // 짝수 줄 ->
            if (i % 2 == 1) {
                for (int k = 0; k < 8; k++) {
                    if (k % 2 == 1) {
                        if (ls.get(i).charAt(k) == 'F') {
                            piece++;
                        }
                    }
                }
            }
        }
        System.out.println(piece);
    }
}
