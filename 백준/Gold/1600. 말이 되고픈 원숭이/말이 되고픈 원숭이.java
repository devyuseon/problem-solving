import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.StringTokenizer;


public class Main {

    static class Node {
        int x;
        int y;
        int cnt;
        int move;

        public Node(int x, int y, int cnt, int move) {
            this.x = x;
            this.y = y;
            this.cnt = cnt;
            this.move = move;
        }
    }

    public static int[] dx = {-1, 1, 0, 0, -2, -2, -1, -1, 1, 1, 2, 2};
    public static int[] dy = {0, 0, -1, 1, -1, 1, -2, 2, -2, 2, -1, 1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int k = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        int w = Integer.parseInt(st.nextToken());
        int h = Integer.parseInt(st.nextToken());
        int[][] matrix = new int[h][w];
        int res = Integer.MAX_VALUE;

        for (int i = 0; i < h; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < w; j++) {
                matrix[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        boolean[][][] visited = new boolean[k + 1][h][w];
        ArrayDeque<Node> dq = new ArrayDeque<>();
        dq.addLast(new Node(0, 0, 0, k));
        visited[k][0][0] = true;

        while (!dq.isEmpty()) {
            Node cur = dq.pollFirst();

            if (cur.x == h - 1 && cur.y == w - 1) {
                res = Math.min(res, cur.cnt);
            }

            for (int i = 0; i < 4; i++) {
                int nx = cur.x + dx[i];
                int ny = cur.y + dy[i];
                if (0 <= nx && nx < h && 0 <= ny && ny < w
                    && matrix[nx][ny] == 0 && !visited[cur.move][nx][ny]) {
                    dq.addLast(new Node(nx, ny, cur.cnt + 1, cur.move));
                    visited[cur.move][nx][ny] = true;
                }
            }

            if (cur.move <= 0) continue;

            for (int i = 4; i < 12; i++) {
                int nx = cur.x + dx[i];
                int ny = cur.y + dy[i];
                int nm = cur.move - 1;
                if (0 <= nx && nx < h && 0 <= ny && ny < w
                        && matrix[nx][ny] == 0 && !visited[nm][nx][ny]) {
                    dq.addLast(new Node(nx, ny, cur.cnt + 1, nm));
                    visited[nm][nx][ny] = true;
                }
            }
        }

        System.out.println(res == Integer.MAX_VALUE ? -1 : res);
    }
}