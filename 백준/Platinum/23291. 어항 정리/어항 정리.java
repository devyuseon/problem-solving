import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;


public class Main {

    public static int n;
    public static int k;
    public static int[][] fishes;
    public static final int MAX_FISH = 10001;
    public static int[] dx = {-1, 1, 0, 0};
    public static int[] dy = {0, 0, -1, 1};
    public static int min;
    public static int max;
    public static int start;
    public static int end;
    public static int height;

    public static void addFish() {
        int min = MAX_FISH;
        for (int i = 1; i < n + 1; i++) {
            if (min > fishes[n][i]) {
                min = fishes[n][i];
            }
        }
        for (int i = 1; i < n + 1; i++) {
            if (min == fishes[n][i]) {
                fishes[n][i]++;
            }
        }
    }

    public static void up() {
        for (int c = 1; c < n; c++) {
            if (fishes[n][c] != 0) {
                fishes[n - 1][c + 1] = fishes[n][c];
                fishes[n][c] = 0;
                break;
            }
        }
    }

    public static void rotate90() {
        while (true) {
            start = 0;
            end = 0;
            height = 0;

            // 시작, 끝 지점 구하기
            for (int j = n; j > 0; j--) {
                if (fishes[n - 1][j] != 0 && end == 0) {
                    end = j;
                }
                if (fishes[n][j] == 0) {
                    start = j + 1;
                    break;
                }
            }

            for (int i = n; i >= 0; i--) {
                if (fishes[i][end] != 0) height++;
                else break;
            }

            // 판단
            if (n - end < height) return;

            int[][] tmp = new int[end - start + 1][height];
            int y = start;
            for (int i = 0; i < end - start + 1; i++) {
                int x = n;
                for (int j = 0; j < height; j++) {
                    tmp[i][j] = fishes[x][y];
                    fishes[x][y] = 0;
                    x--;
                }
                y++;
            }

            int x = n - (end - start + 1);
            y = end + 1;
            for (int i = 0; i < end - start + 1; i++) {
                for (int j = 0; j < height; j++) {
                    fishes[x][y] = tmp[i][j];
                    y++;
                }
                y = end + 1;
                x++;
            }
        }
    }

    public static void divide() {
        int[][] tmp = new int[n + 1][n + 1];
        int[][] visited = new int[n + 1][n + 1];

        for (int i = 0; i < n + 1; i++) {
            for (int j = 0; j < n + 1; j++) {
                if (fishes[i][j] == 0) continue;

                for (int l = 0; l < 4; l++) {
                    int ni = i + dx[l];
                    int nj = j + dy[l];
                    if (ni < 0 || ni >= n + 1 || nj < 0 || nj >= n + 1 || fishes[ni][nj] == 0 || visited[ni][nj] == 1) continue;

                    int d = Math.abs(fishes[i][j] - fishes[ni][nj]) / 5;

                    if (d > 0) {
                        if (fishes[i][j] > fishes[ni][nj]) {
                            tmp[i][j] -= d;
                            tmp[ni][nj] += d;
                        } else {
                            tmp[i][j] += d;
                            tmp[ni][nj] -= d;
                        }
                    }
                }
                visited[i][j] = 1;
            }
        }

        min = MAX_FISH;
        max = 0;
        for (int i = 0; i < n + 1; i++) {
            for (int j = 0; j < n + 1; j++) {
                if (fishes[i][j] == 0) continue;
                fishes[i][j] += tmp[i][j];
                min = Math.min(min, fishes[i][j]);
                max = Math.max(max, fishes[i][j]);
            }
        }
    }

    public static void arrange() {
        int[] tmp = new int[(end - start + 1) * height];
        int idx = 0;
        for (int j = start; j <= end; j++) {
            for (int i = n; i > n - height; i--) {
                tmp[idx] = fishes[i][j];
                fishes[i][j] = 0;
                idx++;
            }
        }

        for (int j = 1; j <= end; j++) {
            fishes[n][j] = tmp[j - 1];
        }
    }

    public static void rotate180() {
        int mid = n / 2;
        for (int i = 0; i < n / 2; i++) {
            fishes[n - 1][mid + 1 + i] = fishes[n][mid - i];
            fishes[n][mid - i] = 0;
        }
        mid = n - (mid / 2);
        int x = n - 2;
        int y = mid + 1;
        for (int i = n - 1; i <= n; i++) {
            for (int j = mid; j > n / 2 ; j--) {
                fishes[x][y] = fishes[i][j];
                fishes[i][j] = 0;
                y++;
            }
            y = mid + 1;
            x--;
        }
        start = mid + 1;
        end = n;
        height = 4;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());
        fishes = new int[n + 1][n + 1];
        st = new StringTokenizer(br.readLine());
        for (int i = 1; i < n + 1; i++) { // 1 ~ n
            fishes[n][i] = Integer.parseInt(st.nextToken());
        }

        int cnt = 0;
        while (true) {
            cnt++;
            addFish();
            up();
            rotate90();
            divide();
            arrange();
            rotate180();
            divide();
            arrange();
            if (max - min <= k) break;
        }

        System.out.println(cnt);
    }
}
