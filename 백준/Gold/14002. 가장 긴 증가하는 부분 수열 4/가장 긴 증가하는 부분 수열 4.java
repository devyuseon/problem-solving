import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;


public class Main {

    public static int n;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] nums = new int[n];
        int[] dp = new int[n];
        int[] memo = new int[n];

        for (int i = 0; i < n; i++) {
            nums[i] = Integer.parseInt(st.nextToken());
            dp[i] = 1;
        }

        int max_idx = 0;
        int max_val = 0;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < i; j++) {
                if (nums[i] > nums[j] && dp[j] + 1 > dp[i]) {
                    dp[i] = dp[j] + 1;
                    memo[i] = j; // i는 j로부터 옴
                }
            }

            if (dp[i] > max_val) {
                max_val = dp[i];
                max_idx = i;
            }
        }

        int[] res = new int[max_val];

        for (int i = max_val - 1; i >= 0; i--) {
            res[i] = nums[max_idx];
            max_idx = memo[max_idx];
        }

        System.out.println(max_val);
        for (int i = 0; i < max_val; i++) {
            System.out.print(res[i] + " ");
        }

    }
}