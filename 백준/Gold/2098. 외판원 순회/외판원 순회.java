import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    public static int n;
    public static int[][] matrix;
    public static int[][] dp;
    public static int end;
    public static final int MAX = 1000000000;

    public static int solution(int now, int visited) {
        if (visited == end) {
            if (matrix[now][0] != 0) {
                return matrix[now][0];
            }
        }

        if (dp[now][visited] != 0) return dp[now][visited];

        dp[now][visited] = MAX;

        // now to i
        for (int i = 0; i < n; i++) {
            // 가는 길이 없음
            if(matrix[now][i] == 0) continue;

            // 이미 방문
            if ((visited & (1 << i)) > 0) continue;

            // solution(i, visited | 1 << i) = i에서 남은 도시를 거쳐 돌아가는 최소 비용
            // dp[now][visited] + now -> i. 이것과
            // now지점에서 남은 도시들을 거쳐 시작점으로 돌아가는 최소 비용을 비교
            int tmp = solution(i, visited | 1 << i); // 방문 처리
            dp[now][visited] = Math.min(dp[now][visited], matrix[now][i] + tmp);
        }

        return dp[now][visited];
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        matrix = new int[n][n];
        dp = new int[n][1 << n];
        end = (1 << n) - 1;

        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                matrix[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        System.out.println(solution(0, 1));
    }
}