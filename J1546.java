import java.util.*;

public class J1546 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        double score[] = new double[sc.nextInt()];

        for (int i = 0; i < score.length; i++) {
            score[i] = sc.nextDouble();
        }

        Arrays.sort(score);
        Double max = score[score.length-1];

        for (int i = 0; i < score.length; i++) {
            score[i] = score[i] / max * 100;
        }

        double sum = 0;
        for (int i = 0; i < score.length; i++) {
            sum += score[i];
        }

        System.out.println(sum/score.length);
    }
}
