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
        long[] nums = new long[n];
        for (int i = 0; i < n; i++) {
            nums[i] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(nums);
        long[] res = new long[3];
        long minAbs = 1000000000L * 3;

        for (int x = 0; x < n - 2; x++) { // x < y < z
            int y = x + 1;
            int z = n - 1;
            while (y < z) {
                long tmp = nums[x] + nums[y] + nums[z];
                if (minAbs > Math.abs(tmp)) {
                    minAbs = Math.abs(tmp);
                    res[0] = nums[x]; res[1] = nums[y]; res[2] = nums[z];
                }
                if (tmp < 0) {
                    y++;
                } else if (tmp > 0) {
                    z--;
                } else {
                    for (int i = 0; i < 3; i++) {
                        System.out.print(res[i] + " ");
                    }
                    System.exit(0);
                }
            }
        }

        for (int i = 0; i < 3; i++) {
            System.out.print(res[i] + " ");
        }
    }
}