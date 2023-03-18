import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

    public static int n;
    public static int m;
    public static int res;
    public static int[][] matrix;
    public static int[][] visited;
    public static int[] dx = {-1, 1, 0, 0};
    public static int[] dy = {0, 0, -1, 1};

    public static int dfs(int x, int y) {
        if (x == m - 1 && y == n - 1) {
            return 1;
        }

        if (visited[x][y] != -1) {
            return visited[x][y];
        }

        visited[x][y] = 0;

        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];

            if (0 <= nx && nx < m && 0 <= ny && ny < n) {
                if (matrix[x][y] > matrix[nx][ny]) {
                    visited[x][y] += dfs(nx, ny);
                }
            }
        }

        return visited[x][y];
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        m = Integer.parseInt(st.nextToken());
        n = Integer.parseInt(st.nextToken());
        matrix = new int[m][n];
        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                matrix[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        visited = new int[m][n];
        for (int i = 0; i < m; i++) {
            Arrays.fill(visited[i], -1);
        }

        dfs(0, 0);

        System.out.println(visited[0][0]);
    }
}