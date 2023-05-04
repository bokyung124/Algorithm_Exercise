import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class J1236 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        //비어있는 라인의 수를 저장 할 변수
        int count = 0;
        //열을 계산하기 위해 입력값을 배열에 저장
        String[] arr = new String[n];

        for(int i = 0; i < n; i++) {
            arr[i] = br.readLine();
            //문자열에 X(경비병)의 포함 여부를 확인. false: 없다는 것
            if(arr[i].contains("X") == false) {
                count++;
            }
        }

        //max 변수에 count 저장 후 count 초기화
        int max = count;
        count = 0;

        //열의 빈 라인을 계산하기 위한 반복문
        for(int i = 0; i < m; i++) {
            //count 하나로 비교까지 하기 부족 -> 같은 역할 하나 더 선언
            int counts = 0;
            for(int j = 0; j < m; j++) {
                if(arr[j].charAt(i) == '.') {
                    counts++;
                }
            }
            //열에 .만 있는지 판별하는 조건문
            if(counts == n) count++;
        }

        //행과 열 중 큰 값을 저장
        max = Math.max(max, count);

        System.out.println(max);
    }

}