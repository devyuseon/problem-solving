import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Main {
    public String S;
    public String T;
    public int res = 0;

    public static void main(String[] args) throws IOException {
        new Main().solution();
    }

    public void solution() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        S = br.readLine();
        T = br.readLine();
        recursion(T);
        bw.write(String.valueOf(res));
        bw.close();
        br.close();
    }

    public void recursion(String t) {
        if (t.equals(S)) {
            res = 1;
            return;
        }
        else if (t.length() < S.length()) {
            return;
        }

        if (t.endsWith("A")) {
            recursion(t.substring(0, t.length() - 1));
        }
        if (t.startsWith("B")) {
            String tmp = t.substring(1);
            StringBuilder sb = new StringBuilder(tmp);
            recursion(sb.reverse().toString());
        }
    }
}