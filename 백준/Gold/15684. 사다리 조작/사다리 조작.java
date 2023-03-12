import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;


public class Main {

    public static int n;
    public static int m;
    public static int h;
    public static int[][] matrix;

    public static boolean check() {
        for (int c = 1; c < n; c++) {
            int x = 1;
            int y = c;
            for (int r = 0; r < h; r++) {
                if (matrix[x][y] == 1) y++;
                else if (matrix[x][y] == 2) y--;
                x++;
            }
            if (y != c) return false;
        }
        return true;
    }

    public static void dfs(int start, int size, int cnt) {
        if (cnt == size) {
            if (check()) {
                System.out.println(size);
                System.exit(0);
            }
            return;
        }

        for (int i = start; i < h + 1; i++) {
            for (int j = 1; j < n; j++) {
                if (matrix[i][j] == 0 && matrix[i][j + 1] == 0) {
                    // 사다리 놓기
                    matrix[i][j] = 1;
                    matrix[i][j + 1] = 2;
                    dfs(i, size, cnt + 1);
                    // 복구
                    matrix[i][j] = 0;
                    matrix[i][j + 1] = 0;
                }
            }
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        h = Integer.parseInt(st.nextToken());

        matrix = new int[h + 1][n + 1];

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            matrix[a][b] = 1; // 오른쪽
            matrix[a][b + 1] = 2; // 왼쪽
        }

        for (int size = 0; size < 4; size++) {
            dfs(1, size, 0);
        }

        System.out.println(-1);
    }
}