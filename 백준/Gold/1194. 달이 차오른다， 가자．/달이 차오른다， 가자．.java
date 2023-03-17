import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.StringTokenizer;

class Point {
    int x;
    int y;
    int cnt;
    int key;

    public Point(){};

    public Point(int x, int y) {
        this.x = x;
        this.y = y;
    }

    public Point(int x, int y, int cnt, int key) {
        this.x = x;
        this.y = y;
        this.cnt = cnt;
        this.key = key;
    }

    @Override
    public String toString() {
        return "Point{" +
                "x=" + x +
                ", y=" + y +
                ", cnt=" + cnt +
                ", key=" + Integer.toBinaryString(key) +
                '}';
    }
}

public class Main {

    public int[] dx = new int[]{-1, 1, 0, 0};
    public int[] dy = new int[]{0, 0, -1, 1};

    public static void main(String[] args) throws IOException {
        new Main().solution();
    }

    public void solution() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        char[][] matrix = new char[n][m];
        Point minsik = new Point();
        int res = -1;

        for (int i = 0; i < n; i++) {
            String line = br.readLine().strip();
            for (int j = 0; j < m; j++) {
                char tmp = line.charAt(j);
                if (tmp == '0') minsik = new Point(i, j); // 민식 위치
                matrix[i][j] = tmp;
            }
        }

        ArrayDeque<Point> q = new ArrayDeque<>();
        int[][][] visited = new int[(1 << 7) - 1][n][m];
        q.addLast(new Point(minsik.x, minsik.y, 0, 0)); // cnt 는 이동 횟수. 현재 민식 위치 출발점
        visited[0][minsik.x][minsik.y] = 1;

        while (!q.isEmpty()) {
            Point now = q.pollFirst();

            if (matrix[now.x][now.y] == '1') {
                res = now.cnt;
                break;
            }

            for (int i = 0; i < 4; i++) {
                int nx = now.x + dx[i];
                int ny = now.y + dy[i];
                if (nx < 0 || nx >= n || ny < 0 || ny >= m) continue; // 범위 밖
                if (matrix[nx][ny] == '#') continue; // 벽
                if (visited[now.key][nx][ny] == 1) continue; // 방문이미함

                if (65 <= (int)matrix[nx][ny] && (int)matrix[nx][ny] <= 70) { // 문인데 열쇠가 없음
                    if ((now.key & (1 << (int)matrix[nx][ny] - 65)) == 0) {
                        continue;
                    }
                }

                // 열쇠줍기
                int nextKey = now.key;
                if (97 <= (int)matrix[nx][ny] && (int)matrix[nx][ny] <= 102) {
                    nextKey |= (1 << (int)matrix[nx][ny] - 97);
                }

                q.addLast(new Point(nx, ny, now.cnt + 1, nextKey));
                visited[nextKey][nx][ny] = 1;
            }
        }

        System.out.println(res);
    }
}