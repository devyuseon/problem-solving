import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.HashMap;
import java.util.Map;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

class Point {
    int x;
    int y;

    public Point(int x, int y) {
        this.x = x;
        this.y = y;
    }
}

class Shark {
    int x;
    int y;
    int speed;
    int d;
    int size;

    public Shark(int x, int y, int speed, int d, int size) {
        this.x = x;
        this.y = y;
        this.speed = speed;
        this.d = d;
        this.size = size;
    }

    @Override
    public String toString() {
        return "Shark{" +
                "x=" + x +
                ", y=" + y +
                ", speed=" + speed +
                ", d=" + d +
                ", size=" + size +
                '}';
    }
}

public class Main {

    public static int[] dx = {-1, 1, 0, 0}; // 상, 하, 우, 좌
    public static int[] dy = {0, 0, 1, -1};
    public static HashMap<Integer, Integer> changeD = new HashMap<>(){{
       put(0, 1);
       put(1, 0);
       put(2, 3);
       put(3, 2);
    }};

    public static int r;
    public static int c;

    public static ArrayList<Shark> sharks;
    public static int[][] matrix;
    public static HashMap<Integer, PriorityQueue<Shark>> cols;

    public static void inputShark() {

        sharks.sort((o1, o2) -> {
            // x좌표 기준 오름차순 , y 좌표 기준 오름차순, 사이즈 기준 내림차순
            if (o1.x == o2.x) {
                if (o1.y == o2.y) {
                    return Integer.compare(o2.size, o1.size);
                } else {
                    return Integer.compare(o1.y, o2.y);
                }
            } else {
                return Integer.compare(o1.x, o2.x);
            }
        });

        // 상어 같은 칸에 있는 상어 처리
        cols = new HashMap<>();
        //ArrayList<Shark> newShark = new ArrayList<>();

        for (int i = 1; i < c + 1; i++) {
            cols.put(i, new PriorityQueue<>(Comparator.comparingInt(o -> o.x)));
        }

        int[][] check = new int[r + 1][c + 1];

        for (Shark shark: sharks) {
            if (check[shark.x][shark.y] == 0) {
                cols.get(shark.y).add(shark);
                check[shark.x][shark.y] = 1;
            }
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        r = Integer.parseInt(st.nextToken());
        c = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int res = 0;

        matrix = new int[r + 1][c + 1]; // 상어 개수 배열
        sharks = new ArrayList<>();
        cols = new HashMap<>();

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            int s = Integer.parseInt(st.nextToken());
            int d = Integer.parseInt(st.nextToken());
            int z = Integer.parseInt(st.nextToken());
            matrix[x][y]++;
            sharks.add(new Shark(x, y, s, d - 1, z));
        }

        inputShark();

        if (!cols.get(1).isEmpty())
            res += cols.get(1).poll().size;

        for (int p = 2; p < c + 1; p++) {
            sharks.clear();
            for (int i = 1; i < c + 1; i++) {
                sharks.addAll(cols.get(i));
            }

            matrix = new int[r + 1][c + 1];

            for (Shark shark : sharks) {
                int speed = shark.speed;

                if (shark.d == 0 || shark.d == 1) speed %= (r - 1) * 2;
                else speed %= (c - 1) * 2;

                for (int s = 0; s < speed; s++) {
                    int nx = shark.x + dx[shark.d];
                    int ny = shark.y + dy[shark.d];

                    if (nx < 1 || nx > r || ny < 1 || ny > c) {
                        shark.d = changeD.get(shark.d); // 방향 전환
                        nx = shark.x + dx[shark.d];
                        ny = shark.y + dy[shark.d];
                    }

                    shark.x = nx;
                    shark.y = ny;
                }
                matrix[shark.x][shark.y]++;
            }

            inputShark();

            if (!cols.get(p).isEmpty())
                res += cols.get(p).poll().size;

        }

        System.out.println(res);
    }
}