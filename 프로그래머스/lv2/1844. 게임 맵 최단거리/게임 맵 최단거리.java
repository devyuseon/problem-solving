import java.util.ArrayDeque;

class Solution {

    static class Point {
        int x;
        int y;
        int cnt;

        public Point(int x, int y, int cnt) {
            this.x = x;
            this.y = y;
            this.cnt = cnt;
        }
    }

    public int[] dx = {-1, 1, 0, 0};
    public int[] dy = {0, 0, -1, 1};

    public int bfs(int[][] maps, int n, int m) {
        ArrayDeque<Point> dq = new ArrayDeque<>();
        boolean[][] visited = new boolean[n][m];
        dq.addLast(new Point(0, 0, 0));
        visited[0][0] = true;
        int res = 10001;

        while (!dq.isEmpty()) {
            Point now = dq.pollFirst();
            if (now.x == n - 1 && now.y == m - 1) {
                res = Math.min(res, now.cnt);
            }
            for (int i = 0; i < 4; i++) {
                int nx = now.x + dx[i];
                int ny = now.y + dy[i];

                if (nx < 0 || nx >= n || ny < 0 || ny >= m) continue;
                if (visited[nx][ny]) continue;
                if (maps[nx][ny] == 0) continue;

                visited[nx][ny] = true;
                dq.addLast(new Point(nx, ny, now.cnt + 1));
            }
        }

        return (res == 10001) ? -1 : res + 1;
    }

    public int solution(int[][] maps) {
        return bfs(maps, maps.length, maps[0].length);
    }
}