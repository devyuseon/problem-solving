import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.math.BigInteger;
import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Iterator;
import java.util.StringTokenizer;

public class P2407 {

    public static void main(String[] args) throws IOException {
        new Main().solution();
    }

    public void solution() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        BigInteger[] dp = new BigInteger[n + 1];
        dp[0] = BigInteger.ONE;

        for (int i = 1; i < n + 1; i++) {
            dp[i] = dp[i - 1].multiply(new BigInteger(String.valueOf(i)));
        }

        System.out.println(dp[n].divide(dp[n - m].multiply(dp[m])));
    }
}