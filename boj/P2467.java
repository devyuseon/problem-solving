import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    public static int n;

    public static void main(String[] args) throws IOException {
        Main.solution();
    }

    public static void solution() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());

        StringTokenizer st = new StringTokenizer(br.readLine());
        long[] nums = new long[n];
        for (int i = 0; i < n; i++) {
            long m = Long.parseLong(st.nextToken());
            nums[i] = m;
        }
        int start = 0;
        int end = n - 1;

        long min = 2_000_000_000;
        long p = nums[0];
        long q = nums[1];

        while (start < end) {
            long tmp = nums[start] + nums[end];
            if (Math.abs(min) > Math.abs(tmp)) {
                min = tmp;
                p = nums[start];
                q = nums[end];
            }
            if (tmp < 0) {
                start++;
            } else {
                end--;
            }
        }

        System.out.println(p + " " + q);
    }

}