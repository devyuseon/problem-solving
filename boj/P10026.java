import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.HashSet;

public class Main {

    public static int n;
    public static int[][] visited;
    public static String[][] matrix;
    int res = 0;
    public static int[] dx = {-1, 1, 0, 0};
    public static int[] dy = {0, 0, -1, 1};

    public static void main(String[] args) throws IOException {
        new Main().solution();
    }

    public static void dfs(int x, int y, String color) {
        if (!matrix[x][y].equals(color)) return;

        visited[x][y] = 1;

        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];
            if (nx < 0 || nx >= n || ny < 0 || ny >= n || visited[nx][ny] == 1) continue;
            dfs(nx, ny, color);
        }
    }

    public void solution() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        StringBuilder sb = new StringBuilder();

        matrix = new String[n][n];
        visited = new int[n][n];
        HashMap<String, Integer> colors = new HashMap<>();
        colors.put("R", 0);
        colors.put("G", 0);
        colors.put("B", 0);

        for (int i = 0; i < n; i++) {
            String line = br.readLine();
            for (int j = 0; j < n; j++) {
                matrix[i][j] = String.valueOf(line.charAt(j));
            }
        }

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (visited[i][j] == 0) {
                    dfs(i, j, matrix[i][j]);
                    colors.put(matrix[i][j], colors.get(matrix[i][j]) + 1);
                }
            }
        }

        int res = 0;
        for (String k: colors.keySet()) {
            res += colors.get(k);
        }
        sb.append(res).append(" ");

        visited = new int[n][n];
        colors = new HashMap<>();
        colors.put("R", 0);
        colors.put("G", 0);
        colors.put("B", 0);

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (matrix[i][j].equals("R")) {
                    matrix[i][j] = "G";
                }
            }
        }

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (visited[i][j] == 0) {
                    dfs(i, j, matrix[i][j]);
                    colors.put(matrix[i][j], colors.get(matrix[i][j]) + 1);
                }
            }
        }

        res = 0;
        for (String k: colors.keySet()) {
            res += colors.get(k);
        }
        sb.append(res);

        System.out.println(sb);
    }
}