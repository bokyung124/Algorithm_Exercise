import java.util.*;

public class J1212_test {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int eight = sc.nextInt();
        String e = Integer.toString(eight);     // 8진수 string 변환
        int index = (int) Math.log10(eight);    // 8진수 뒤에서부터 한자리씩 가져오기 위한 인덱스
        int num = 0;                            // 10진수
        ArrayList<Integer> remainder = new ArrayList<>();   // 10진수 2로 나눈 나머지 배열

        // 8진수 -> 10진수
        for (int i = 1; i <= (Math.log10(eight)+1); i++) {
            String a = e.substring(index, index+1);
            int b = (int) (Integer.parseInt(a) * Math.pow(8, i-1));
            index--;
            num += b;
        }

        // 10진수 -> 2진수
        while (true) {
            remainder.add(num%2);
            if (num < 2)
                break;
            num /= 2;
        }

        // 10진수 2로 나눈 나머지 배열 거꾸로 출력
        for (int i = remainder.size()-1; i >= 0; i--)
            System.out.print(remainder.get(i));
    }
}
