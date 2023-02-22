import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.StringTokenizer;

class Edge {
    int start;
    int end;
    int cost;

    public Edge(int start, int end, int cost) {
        this.start = start;
        this.end = end;
        this.cost = cost;
    }

    @Override
    public String toString() {
        return "Edge{" +
                "start=" + start +
                ", end=" + end +
                ", cost=" + cost +
                '}';
    }
}

public class P6497 {

    public static int[] parent;
    public static int[] rank;

    public static void main(String[] args) throws IOException {
        new Main().solution();
    }

    public static void union(int x, int y) {
        x = find(x);
        y = find(y);

        if (rank[x] > rank[y]) { // 레벨이 작은 y가 레벨이 큰 x 밑으로
            parent[y] = x;
        } else if (rank[y] > rank[x]) {
            parent[x] = y;
        } else {
            parent[x] = y;
            rank[y] += 1;
        }
    }

    public static int find(int x) {
        if (parent[x] != x) {
            parent[x] = find(parent[x]);
        }
        return parent[x];
    }

    public static boolean isUnion(int x, int y) {
        return find(x) == find(y);
    }

    public void solution() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        while (true) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int m = Integer.parseInt(st.nextToken());
            int n = Integer.parseInt(st.nextToken());
            if (n == 0 && m == 0) break;

            ArrayList<Edge> edges = new ArrayList<>();
            parent = new int[m + 1];
            rank = new int[m + 1];
            int res = 0;
            int total = 0;

            for (int i = 1; i < m + 1; i++) {
                parent[i] = i;
            }

            for (int i = 0; i < n; i++) {
                st = new StringTokenizer(br.readLine());
                int x = Integer.parseInt(st.nextToken());
                int y = Integer.parseInt(st.nextToken());
                int z = Integer.parseInt(st.nextToken());
                edges.add(new Edge(x, y, z));
                total += z;
            }

            edges.sort(Comparator.comparingInt(o -> o.cost));

            int cnt = 0;
            for (Edge edge : edges) {
                if (!isUnion(edge.start, edge.end)) {
                    union(edge.start, edge.end);
                    res += edge.cost;
                    cnt++;
                }
                if (cnt == m - 1) break;
            }

            System.out.println(total - res);
        }

    }
}