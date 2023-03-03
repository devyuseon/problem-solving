import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.HashMap;
import java.util.StringTokenizer;

public class Main {

    public static boolean binarySearch(int target, int[] arr) {
        int s = 0;
        int e = arr.length - 1;
        int mid;

        while (s <= e) {
            mid = (s + e) / 2;

            if (arr[mid] == target) {
                return true;
            } else if (target < arr[mid]) {
                e = mid - 1;
            } else {
                s = mid + 1;
            }

        }
        return false;
    }

    public static void getPrefixSum(int[] C, int[] c) {
        int idx = 0;
        for (int i = 0; i < C.length; i++) {
            int sum = 0;
            for (int j = i; j < C.length; j++) {
                sum += C[j];
                c[idx++] = sum;
            }
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());

        // A
        int n = Integer.parseInt(br.readLine());
        int[] A = new int[n];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            A[i] = Integer.parseInt(st.nextToken());
        }

        // B
        int m = Integer.parseInt(br.readLine());
        int[] B = new int[m];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < m; i++) {
            B[i] = Integer.parseInt(st.nextToken());
        }

        // 누적합 구하기
        int[] a = new int[n * (n + 1) / 2];
        int[] b = new int[m * (m + 1) / 2];
        getPrefixSum(A, a);
        getPrefixSum(B, b);

        // 누적합 배열 정렬
        Arrays.sort(a);
        Arrays.sort(b);

        HashMap<Integer, Integer> counting = new HashMap<>();
        for (int k: b) {
            if (!counting.containsKey(k)) counting.put(k, 1);
            else counting.put(k, counting.get(k) + 1);
        }

        long cnt = 0;

        for (int k: a) {
            int tmp = t - k;
            if (binarySearch(tmp, b)) {
                cnt += counting.get(tmp);
            }
        }

        System.out.println(cnt);
    }
}