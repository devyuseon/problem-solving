import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.StringTokenizer;

class Node {
    public int v;
    public int cost;

    public Node(int v, int cost) {
        this.v = v;
        this.cost = cost;
    }
}

public class Main {

    public static HashMap<Integer, ArrayList<Node>> graph;
    public static int v;
    public static Node node = new Node(1, 0);

    public static void main(String[] args) throws IOException {
        Main.solution();
    }

    public static void dfs(int start) {
        ArrayDeque<Node> s = new ArrayDeque<>();
        s.addLast(new Node(start, 0)); // 정점, cost
        int[] visited = new int[v + 1];

        while (!s.isEmpty()) {
            Node now = s.pollLast();
            visited[now.v] = 1;
            if (node.cost < now.cost) {
                node = now;
            }
            for (Node next : graph.get(now.v)) {
                if (visited[next.v] == 0) {
                    s.addLast(new Node(next.v, now.cost + next.cost));
                }
            }
        }
    }

    public static void solution() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        v = Integer.parseInt(br.readLine());

        if (v == 1) {
            System.out.println(0);
            return;
        }

        graph = new HashMap<>();
        for (int i = 0; i < v - 1; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int s = Integer.parseInt(st.nextToken()); // 정점 번호
            int e = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());

            if (!graph.containsKey(s)) {
                graph.put(s, new ArrayList<>());
            }
            if (!graph.containsKey(e)) {
                graph.put(e, new ArrayList<>());
            }

            graph.get(s).add(new Node(e, c)); // 도착점, 비용
            graph.get(e).add(new Node(s, c)); // 무방향 그래프

        }

        dfs(1);
        dfs(node.v);

        System.out.println(node.cost);
    }

}