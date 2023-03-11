import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.StringTokenizer;

class Point {
    int x;
    int y;
    int d;

    public Point(int x, int y, int d) {
        this.x = x;
        this.y = y;
        this.d = d;
    }
}

public class Main {

    public static int n;
    public static int m;
    public static HashMap<Integer, List<List<Integer>>> dir = new HashMap<>();
    public static int[] dx = {-1, 1, 0, 0};
    public static int[] dy = {0, 0, -1, 1}; // 상, 하, 좌, 우
    public static ArrayList<Point> cctv = new ArrayList<>();
    public static ArrayList<int[]> res = new ArrayList<>();

    public static void dfs (int idx, int[] tmp) {
        if (idx == cctv.size()) {
            res.add(tmp);
            return;
        }

        for (int i = 0; i < dir.get(cctv.get(idx).d).size(); i++) {
            int[] next = new int[cctv.size()];
            for (int j = 0; j < cctv.size(); j++) {
                next[j] = tmp[j];
            }
            next[idx] = i;
            dfs(idx + 1, next);
        }
    }


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        dir.put(1, List.of(List.of(0), List.of(1), List.of(2), List.of(3))); // 4가지
        dir.put(2, List.of(List.of(0, 1), List.of(2, 3))); // 2가지
        dir.put(3, List.of(List.of(0, 3), List.of(3, 1), List.of(1, 2), List.of(2, 0))); // 4가지
        dir.put(4, List.of(List.of(2, 0, 3), List.of(0, 3, 1), List.of(3, 1, 2), List.of(1, 2, 0))); // 3가지
        dir.put(5, List.of(List.of(0, 1, 2, 3))); // 1가지

        int[][] matrix = new int[n][m];
        int answer = n * m;

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < m; j++) {
                int tmp = Integer.parseInt(st.nextToken());

                if (1 <= tmp && tmp <= 5) { // cctv
                    cctv.add(new Point(i, j, tmp));
                }

                matrix[i][j] = tmp;
            }
        }

        dfs(0, new int[cctv.size()]);

        for (int i = 0; i < res.size(); i++) {
            // 한 경우의 수
            int[] tmp = res.get(i);
            int[][] tmpBoard = new int[n][m];
            for (int j = 0; j < n; j++) {
                for (int k = 0; k < m; k++) {
                    tmpBoard[j][k] = matrix[j][k];
                }
            }

            for (int j = 0; j < cctv.size(); j++) {
                // 한 cctv 방향
                List<Integer> directions = dir.get(cctv.get(j).d).get(tmp[j]);
                for (Integer d : directions) {
                    int x = cctv.get(j).x;
                    int y = cctv.get(j).y;
                    while (true) {
                        x += dx[d];
                        y += dy[d];

                        if (x < 0 || x >= n || y < 0 || y >= m || matrix[x][y] == 6) break;
                        if (1 <= matrix[x][y] && matrix[x][y] <= 5) continue;

                        tmpBoard[x][y] = -1; // 감시가능 표시
                    }
                }
            }

            int cnt = 0;
            for (int j = 0; j < n; j++) {
                for (int k = 0; k < m; k++) {
                    if (tmpBoard[j][k] == 0) cnt++;
                }
            }

            answer = Math.min(answer, cnt);
        }

        System.out.println(answer);
    }
}