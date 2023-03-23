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
        int[] lis = new int[n];
        int[] memo = new int[n];
        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < n; i++) {
            nums[i] = Integer.parseInt(st.nextToken());
        }

        int size = 0;
        for (int i = 0; i < n; i++) {
            int idx = Arrays.binarySearch(lis, 0, size, nums[i]);
            if (idx < 0) idx = idx * (-1) - 1;
            memo[i] = idx;
            lis[idx] = nums[i];
            if (idx == size) size++;
        }

        int idx = size - 1;
        int[] answer = new int[size];

        for (int i = n - 1; i >= 0; i--) {
            if (memo[i] == idx) {
                answer[idx--] = nums[i];
            }
        }

        sb.append(size).append("\n");
        for (int i = 0; i < size; i++) {
            sb.append(answer[i]).append(" ");
        }

        System.out.println(sb);
    }
}