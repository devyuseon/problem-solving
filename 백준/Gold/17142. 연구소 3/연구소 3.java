import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.StringTokenizer;

class Point {
    int x;
    int y;
    int t;

    public Point(int x, int y) {
        this.x = x;
        this.y = y;
    }

    public Point(int x, int y, int t) {
        this.x = x;
        this.y = y;
        this.t = t;
    }

    @Override
    public String toString() {
        return "Point{" +
                "x=" + x +
                ", y=" + y +
                '}';
    }
}

public class Main {

    public static int n;
    public static int m;
    public static ArrayList<Point> virus;
    public static int[][] matrix;
    public static int res = 1_000_000_000;
    public static int[] dx = {-1, 1, 0, 0};
    public static int[] dy = {0, 0, -1, 1};

    public static boolean isIn (int x, int y) {
        if (0 <= x && x < n && 0 <= y && y < n) return true;
        else return false;
    }

    public static boolean check (boolean[][] visited) {
        boolean isSpread = true;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (matrix[i][j] == 0) {
                    if (!visited[i][j]) {
                        isSpread = false;
                        break;
                    }
                }
            }
            if (!isSpread) break;
        }
        return isSpread;
    }

    public static void spread(ArrayDeque<Point> active) {
        boolean[][] visited = new boolean[n][n];
        ArrayDeque<Point> dq = new ArrayDeque<>();
        for (Point p : active) {
            visited[p.x][p.y] = true;
            dq.add(new Point(p.x, p.y, 0));
        }

        int time = 0;
        boolean isSpread = false;

        while (!dq.isEmpty()) {
            if (check(visited)) {
                for (Point p: dq)
                    time = Math.max(time, p.t);
                isSpread = true;
                break;
            }

            Point now = dq.pollFirst();

            for (int i = 0; i < 4; i++) {
                int nx = now.x + dx[i];
                int ny = now.y + dy[i];

                if (isIn(nx, ny) && !visited[nx][ny] && matrix[nx][ny] != 1) {
                    visited[nx][ny] = true;
                    dq.add(new Point(nx, ny, now.t + 1));
                }
            }
        }

        if (isSpread) {
            res = Math.min(res, time);
        }
    }

    public static void combination(int start, int r, ArrayDeque<Point> active) { // nCr
        if (r == 0) {
            spread(active);
        }

        for (int i = start; i < virus.size(); i++) {
            active.addLast(virus.get(i));
            combination(i + 1, r - 1, active);
            active.pollLast();
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        matrix = new int[n][n];
        virus = new ArrayList<>();


        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                int tmp = Integer.parseInt(st.nextToken());

                if (tmp == 2)
                    virus.add(new Point(i, j));

                matrix[i][j] = tmp;
            }
        }

        combination(0, m, new ArrayDeque<>());

        if (res == 1_000_000_000) {
            System.out.println(-1);
        } else {
            System.out.println(res);
        }
    }
}