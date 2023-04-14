import java.util.*;

public class J2693 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = Integer.parseInt(sc.nextLine());
        ArrayList<Integer> array = new ArrayList<>();
        ArrayList<Integer> result = new ArrayList<>();

        for(int i = 0; i < n; i++) {
            String str = sc.nextLine();
            StringTokenizer st = new StringTokenizer(str, " ");
            while(st.hasMoreTokens()) {
                array.add(Integer.parseInt(st.nextToken()));
            }
            int size = array.size();
            Collections.sort(array);
            result.add(array.get(size-3));
            array.clear();
        }

        for(int i = 0; i < result.size(); i++) {
            System.out.println(result.get(i));
        }
    }
}
