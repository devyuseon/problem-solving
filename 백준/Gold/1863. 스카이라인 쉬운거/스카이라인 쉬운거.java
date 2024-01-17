import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int answer = 0;
        ArrayDeque<Integer> stack = new ArrayDeque<>();

        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());

            while (!stack.isEmpty() && stack.peekLast() >= b) {
                if (stack.peekLast() > b) answer++;
                stack.pollLast();
            }
            stack.addLast(b);
        }

        while (!stack.isEmpty() && stack.peekLast() >= 0) {
            if (stack.peekLast() > 0) answer++;
            stack.pollLast();
        }

        System.out.println(answer);
    }
}