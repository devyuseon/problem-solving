import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    public static int n;
    public static int m;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());


        int[] M = new int[n];
        int[] C = new int[n];

        st = new StringTokenizer(br.readLine());
        StringTokenizer st1 = new StringTokenizer(br.readLine());
        int total = 0;

        for (int i = 0; i < n; i++) {
            M[i] = Integer.parseInt(st.nextToken());
            C[i] = Integer.parseInt(st1.nextToken());
            total += C[i];
        }

        int[] dp = new int[total + 1];

        for (int i = 0; i < n; i++) {
            for (int j = total; j >= 0 ; j--) {
                if (j - C[i] < 0) continue;
                dp[j] = Math.max(dp[j], dp[j - C[i]] + M[i]);
                // i번째 앱을 포함 X , i번째 앱을 안넣었을때 에서 i번째를 포함했을 때
            }
        }

        int res = total;
        for (int i = 0; i < total + 1; i++) {
            if (dp[i] >= m) {
                res = i;
                break;
            }
        }

        System.out.println(res);
    }
}