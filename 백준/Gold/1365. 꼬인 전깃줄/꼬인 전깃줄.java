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
        for (int i = 0; i < n; i++) {
            nums[i] = Integer.parseInt(st.nextToken());
        }

        int[] list = new int[n];

        int size = 0;
        for (int i = 0; i < n; i++) {
            int idx = Arrays.binarySearch(list, 0, size, nums[i]);
            if (idx < 0) idx = idx * (-1) - 1;
            list[idx] = nums[i];
            if (idx == size) size++; // 끝에 들어갔을 경우
        }

        System.out.println(n - size);
    }
}