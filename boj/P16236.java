import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.StringTokenizer;

class Fish {
    public int x;
    public int y;
    public int size;
    public int cost;

    public Fish(int x, int y, int size) {
        this.x = x;
        this.y = y;
        this.size = size;
    }

    public Fish(int x, int y, int size, int cost) {
        this.x = x;
        this.y = y;
        this.size = size;
        this.cost = cost;
    }

}

public class P16236 {

    public static int n;
    public static int[][] matrix;
    public static Fish shark;
    public static int eat = 0;
    public static HashMap<Fish, Integer> fishes;
    public static int[] dx = {-1, 1, 0, 0};
    public static int[] dy = {0, 0, -1, 1};

    public static void main(String[] args) throws IOException {
        Main.solution();
    }

    public static ArrayList<Fish> bfs() {
        ArrayDeque<Fish> q = new ArrayDeque<>();
        ArrayList<Fish> res = new ArrayList<>();
        q.addLast(new Fish(shark.x, shark.y, shark.size, 0));
        int[][] visited = new int[n][n];
        visited[shark.x][shark.y] = 1;

        while (!q.isEmpty()) {
            Fish now = q.pollFirst();

            for (int i = 0; i < 4; i++) {
                int nx = now.x + dx[i];
                int ny = now.y + dy[i];
                if (0 <= nx && nx < n && 0 <= ny && ny < n && visited[nx][ny] == 0) {
                    if (matrix[nx][ny] > shark.size) continue;

                    Fish fish = new Fish(nx, ny, matrix[nx][ny], now.cost + 1);
                    q.addLast(fish); // size는 의미 x
                    visited[nx][ny] = 1;

                    if (matrix[nx][ny] > 0 && matrix[nx][ny] < shark.size) {// 먹을 수 있음
                        res.add(fish);
                    }
                }
            }
        }
        return res;
    }

    public static void solution() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        matrix = new int[n][n]; // 물고기 위치, 크기
        int sec = 0; // 시간
        fishes = new HashMap<>(); // 물고기 위치, 물고기까지 가는데 걸리는 거리

        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                int tmp = Integer.parseInt(st.nextToken());
                if (tmp == 9) { // 아기상어 위치
                    shark = new Fish(i, j, 2);
                } else if (tmp > 0 && tmp < 7) {
                    matrix[i][j] = tmp;
                    fishes.put(new Fish(i, j, tmp), 0);
                }
            }
        }

        while(true) {
            ArrayList<Fish> candi = bfs();
            if (candi.isEmpty()) break;
            if (candi.size() != 1) {
                Collections.sort(candi, (o1, o2) -> {
                    if (o1.cost == o2.cost) {
                        if (o1.x == o2.x) {
                            return Integer.compare(o1.y, o2.y); // y좌표 오름차순
                        } else {
                            return Integer.compare(o1.x, o2.x); // x좌표 오름차순
                        }
                    } else {
                        return Integer.compare(o1.cost, o2.cost); // 비용 오름차순
                    }
                });
            }

            Fish fish = candi.get(0);
            sec += fish.cost;
            matrix[fish.x][fish.y] = 0;
            eat += 1;
            shark.x = fish.x;
            shark.y = fish.y;
            if (eat == shark.size) {
                shark.size += 1;
                eat = 0;
            }
        }

        System.out.println(sec);
    }

}