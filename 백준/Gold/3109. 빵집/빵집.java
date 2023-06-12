import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;


public class Main {

    public static int r;
    public static int c;
    public static int[] dx = {-1, 0, 1}; // 오른쪽, 오른쪽 위 대각선, 오른쪽 아래 대각선
    public static int[] dy = {1, 1, 1};
    public static char[][] matrix;
    public static boolean[][] visited;

    public static boolean dfs(int x, int y) {
        if (y == c - 1) {
            return true;
        }

        for (int i = 0; i < 3; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];
            if (0 <= nx && nx < r && 0 <= ny && ny < c &&
                !visited[nx][ny] && matrix[nx][ny] == '.') {
                visited[nx][ny] = true;
                if (dfs(nx, ny)) return true;
            }
        }

        return false;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        r = Integer.parseInt(st.nextToken());
        c = Integer.parseInt(st.nextToken());
        matrix = new char[r][c];
        visited = new boolean[r][c];
        for (int i = 0; i < r; i++) matrix[i] = br.readLine().toCharArray();

        int cnt = 0;
        for (int i = 0; i < r; i++) {
            if (matrix[i][0] == 'x') continue;
            if (dfs(i, 0)) cnt++;
        }

        System.out.println(cnt);
    }
}