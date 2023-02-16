import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.StringTokenizer;

class Point {
    public int x;
    public int y;
    public int z;

    public Point(int x, int y, int z) {
        this.x = x;
        this.y = y;
        this.z = z;
    }
}

public class P2206 {

    public static int n;
    public static int m;
    public static int[][] matrix;
    public static int[] dx = {-1, 1, 0, 0};
    public static int[] dy = {0, 0, -1, 1};

    public static void main(String[] args) throws IOException {
        Main.solution();
    }

    public static void solution() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        matrix = new int[n][m];
        int res = -1;

        for (int i = 0; i < n; i++) {
            String line = br.readLine();
            for (int j = 0; j < m; j++) {
                matrix[i][j] = line.charAt(j) - '0';
            }
        }

        ArrayDeque<Point> q = new ArrayDeque<>();
        q.addLast(new Point(0, 0, 0));
        int[][][] visited = new int[n][m][2];
        visited[0][0][0] = 1;

        while (!q.isEmpty()) {
            Point now = q.pollFirst();

            if (now.x == n - 1 && now.y == m - 1) {
                res = visited[n - 1][m - 1][now.z];
                break;
            }

            for (int i = 0; i < 4; i++) {
                int nx = now.x + dx[i];
                int ny = now.y + dy[i];
                if (0 <= nx && nx < n && 0 <= ny && ny < m) {
                    // 벽이고, 아직 깬 적 없음
                    if (matrix[nx][ny] == 1 && now.z == 0) {
                        visited[nx][ny][1] = visited[now.x][now.y][0] + 1;
                        q.addLast(new Point(nx, ny, 1));
                    } else if (matrix[nx][ny] == 0 && visited[nx][ny][now.z] == 0) {
                        // 벽이 아님
                        visited[nx][ny][now.z] = visited[now.x][now.y][now.z] + 1;
                        q.addLast(new Point(nx, ny, now.z));
                    }
                }
            }
        }

        System.out.println(res);
    }

}