import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class P1932 {
    public static void main(String[] args) throws IOException {
        Main.solution();
    }

    public static void solution() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        int[][] nums = new int[n][];
        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            nums[i] = new int[i + 1];
            for (int j = 0; j < i + 1; j++) {
                nums[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        for (int i = 1; i < n; i++) {
            nums[i][0] += nums[i - 1][0];
            for (int j = 1; j < i; j++) {
                nums[i][j] = Math.max(nums[i - 1][j - 1] + nums[i][j], nums[i - 1][j] + nums[i][j]);
            }
            nums[i][i] += nums[i - 1][i - 1];
        }

        int res = 0;
        for (int i = 0; i < n; i++) {
            res = Math.max(res, nums[n - 1][i]);
        }
        System.out.println(res);
    }
}