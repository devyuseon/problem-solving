import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.StringTokenizer;


public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int[] inDegree = new int[n + 1];
        HashMap<Integer, HashSet<Integer>> graph = new HashMap<>();
        StringBuilder sb = new StringBuilder();
        int cnt = 0;

        for (int i = 1; i < n + 1; i++) {
            graph.put(i, new HashSet<>());
        }
        for (int i = 0; i < m; i++) {
            String[] pd = br.readLine().split(" ");
            for (int j = 2; j < pd.length; j++) {
                int prev = Integer.parseInt(pd[j - 1]);
                int next = Integer.parseInt(pd[j]);
                HashSet<Integer> tmp = graph.get(prev);
                if (!tmp.contains(next)) {
                    tmp.add(next);
                    inDegree[next]++;
                }

            }
        }
        ArrayDeque<Integer> dq = new ArrayDeque<>();
        for (int i = 1; i < n + 1; i++) {
            if (inDegree[i] == 0) {
                dq.addLast(i);
            }
        }

        while (!dq.isEmpty()) {
            int cur = dq.pollFirst();
            sb.append(cur).append("\n");
            cnt++;

            for (int v : graph.get(cur)) {
                inDegree[v]--;

                if (inDegree[v] == 0) {
                    dq.addLast(v);
                }
            }
        }

        if (cnt == n) {
            System.out.println(sb);
        } else {
            System.out.println(0);
        }
    }
}