import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class P9663 {

    public static int res = 0;
    public static int n;
    public static final int MAX = 14;
    public static int[] col = new int[MAX + 1];

    public static void main(String[] args) throws IOException {
        Main.solution();
    }

    public static void nqueen(int m) {
        if (m == n) { // n개를 다 놓음
            res++;
        } else {
            for (int i = 0; i < n; i++) {
                col[m] = i; // m열에 퀸을 배치
                if(check(m)) nqueen(m + 1); // m열에 퀸을 놓을 수 있다면 다음 열로 넘어감
            }
        }
    }

    private static boolean check(int m) {
        for (int i = 0; i < m; i++) {
            // col[i] == col[m] i열의 행과 m열의 행이 일치 -> 놓을 수 없음
            // Math.abs(col[m] - col[i]) == m - i -> abs(행 - 행) == abs(열 - 열) -> 같은 대각선
            if (col[i] == col[m] || Math.abs(col[m] - col[i]) == m - i)
                return false;
        }
        return true;
    }

    public static void solution() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        nqueen(0);
        System.out.println(res);
    }

}