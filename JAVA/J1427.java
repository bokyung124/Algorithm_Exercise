import java.util.*;

public class J1427 {
    public static void main (String[] args){
        Scanner sc = new Scanner(System.in);
        ArrayList<Integer> arr = new ArrayList<>();

        int num = Integer.parseInt(sc.nextLine());

        for (int i = (int) (Math.log10(num)); i >= 1; i--) {
            arr.add((int) (num/Math.pow(10, i)));
            num = (int) (num%Math.pow(10, i));
        }
        arr.add(num);

        Collections.sort(arr);

        int result = 0;
        int j = arr.size()-1;
        for (int i = arr.size()-1; i >= 0; i--) {
            result += arr.get(i) * Math.pow(10, j);
            j--;
        }
        System.out.print(result);
    }
}
