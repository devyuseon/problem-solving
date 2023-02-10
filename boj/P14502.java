import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.StringTokenizer;

class Pair {

    public int x;
    public int y;

    public Pair(int x, int y) {
        this.x = x;
        this.y = y;
    }

    @Override
    public String toString() {
        return "(" + x + ", " + y + ")";
    }
}


public class P14502 {

    public static int n;
    public static int m;
    public static int[][] matrix;
    public static ArrayList<Pair> empty = new ArrayList<>();
    public static ArrayList<Pair> virus = new ArrayList<>();
    public static int res;
    public static int[] dx = new int[]{-1, 1, 0, 0};
    public static int[] dy = new int[]{0, 0, -1, 1};

    public static void main(String[] args) throws IOException {
        Main.solution();
    }

    public static void count(int[][] tmp) {
        int size = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (tmp[i][j] == 0) {
                    size++;
                }
            }
        }
        res = Math.max(res, size);
    }

    public static void bfs(int[][] tmp) {
        ArrayDeque<Pair> q = new ArrayDeque<>();

        for (Pair pair : virus) {
            q.addLast(pair);
        }

        while (!q.isEmpty()) {
            Pair now = q.pollFirst();

            for (int i = 0; i < 4; i++) {
                int nx = now.x + dx[i];
                int ny = now.y + dy[i];

                if (0 <= nx && nx < n && 0 <= ny && ny < m) {
                    if (tmp[nx][ny] == 0) {
                        tmp[nx][ny] = 2;
                        q.addLast(new Pair(nx, ny));
                    }
                }
            }

        }

        count(tmp);

    }

    public static void getSafeZone(ArrayList<Pair> candi) {
        int[][] tmp = new int[n][m];

        for (int i = 0; i < n; i++) {
            tmp[i] = matrix[i].clone();
        }

        for (Pair pair : candi) {
            tmp[pair.x][pair.y] = 1;
        }

        bfs(tmp);

    }

    public static void combination(ArrayList<Pair> candi, int cnt, int start) {
        if (cnt == 3) {
            getSafeZone(candi);
        } else {
            for (int i = start; i < empty.size(); i++) {
                candi.add(empty.get(i));
                combination(candi, cnt + 1, i + 1);
                candi.remove(candi.size() - 1);
            }
        }
    }

    public static void solution() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        matrix = new int[n][m];

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < m; j++) {
                matrix[i][j] = Integer.parseInt(st.nextToken());

                if (matrix[i][j] == 0) { // 빈칸
                    empty.add(new Pair(i, j));
                } else if (matrix[i][j] == 2) { // 바이러스
                    virus.add(new Pair(i, j));
                }
            }
        }

        combination(new ArrayList<>(), 0, 0);
        System.out.println(res);
    }

}