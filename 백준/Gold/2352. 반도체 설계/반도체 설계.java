import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;


public class Main {

    public static int n;
    public static final int MAX = 40_000;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] nums = new int[n];
        for (int i = 0; i < n; i++) {
            nums[i] = Integer.parseInt(st.nextToken());
        }

        int[] memo = new int[n];
        Arrays.fill(memo, MAX + 1);
        int size = 1;
        memo[0] = nums[0];
        for (int i = 1; i < n; i++) {
            // 이번 숫자가 memo배열의 끝보다 크면 추가
            if (nums[i] > memo[size - 1]) {
                memo[size++] = nums[i];
            } else {
                int idx = Arrays.binarySearch(memo, nums[i]);
                if (idx < 0) {
                    idx = idx * (-1) - 1;
                    memo[idx] = nums[i];
                }
            }
        }

        System.out.println(size);
    }
}