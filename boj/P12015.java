import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class P12015 {

    public static int[] nums;
    public static int[] lis;

    public static void main(String[] args) throws IOException {
        new Main().solution();
    }

    public static int binarySearch(int left, int right, int target) {
        int mid;
        while (left < right) {
            mid = (left + right) / 2;
            if (lis[mid] < target) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }
        return right;
    }

    public void solution() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        nums = new int[n];
        lis = new int [n];

        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            nums[i] = Integer.parseInt(st.nextToken());
        }
        lis[0] = nums[0];
        int last = 0;

        for (int i = 1; i < n; i++) {
            if (lis[last] < nums[i]) {
                lis[last + 1] = nums[i];
                last++;
            } else {
                int idx = binarySearch(0, last, nums[i]);
                lis[idx] = nums[i];
            }
        }

        System.out.println(last + 1);
    }
}