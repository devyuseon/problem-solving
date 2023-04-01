import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;


public class Main {

    public static int n;
    public static int m;
    public static int[][] matrix;
    public static int[][] tmp;
    public static boolean[][] visited;
    public static int[] dx = {-1, 1, 0, 0};
    public static int[] dy = {0, 0, -1, 1};

    public static void dfs(int x, int y) {
        visited[x][y] = true;

        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];

            if (nx < 0 || nx >= n || ny < 0 || ny >= m) continue;
            if (visited[nx][ny]) continue;
            if (matrix[nx][ny] == 1) tmp[nx][ny]++; // 외부 치즈 표시
            else dfs(nx, ny);
        }
    }

    public static boolean melting() {
        tmp = new int[n][m];
        visited = new boolean[n][m];
        dfs(0, 0);

        boolean allMelted = true;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (tmp[i][j] >= 2) matrix[i][j] = 0;
                if (matrix[i][j] > 0) allMelted = false;
            }
        }

        return allMelted;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        matrix = new int[n][m];

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < m; j++) {
                matrix[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        int res = 0;
        while (true) {
            boolean allMelted = melting();
            res++;
            if (allMelted) break;
        }

        System.out.println(res);

    }
}