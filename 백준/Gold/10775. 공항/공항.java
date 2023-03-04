import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;


public class Main {

    public static int[] gates;

    public static int find(int x) {
        if (gates[x] != x) {
            gates[x] = find(gates[x]);
        }
        return gates[x];
    }

    public static void union(int x, int y) {
        x = find(x);
        y = find(y);

        gates[x] = y;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int g = Integer.parseInt(br.readLine());
        int p = Integer.parseInt(br.readLine());
        int res = 0;

        gates = new int[g + 1];
        for (int i = 0; i <= g; i++) {
            gates[i] = i;
        }

        for (int i = 0; i < p; i++) {
            int n = find(Integer.parseInt(br.readLine()));
            if (n == 0) break;
            union(n, n - 1);
            res++;
        }
        System.out.println(res);
    }
}