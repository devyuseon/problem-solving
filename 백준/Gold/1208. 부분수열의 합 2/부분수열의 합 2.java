import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.StringTokenizer;


public class Main {

    public static int n;
    public static int s;
    public static ArrayList<Long> front;
    public static ArrayList<Long> back;

    public static ArrayList<Long> getSum(ArrayList<Long> nums) {
        ArrayList<Long> sums = new ArrayList<>();
        for (int i = 0; i < (1 << nums.size()); i++) {
            long sum = 0;
            for (int j = 0; j < nums.size(); j++) {
                if (((i & (1 << j))) > 0) {
                    sum += nums.get(j);
                }
            }
            sums.add(sum);
        }
        return sums;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        s = Integer.parseInt(st.nextToken());
        front = new ArrayList<>();
        back = new ArrayList<>();
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n / 2; i++) {
            front.add(Long.parseLong(st.nextToken()));
        }
        for (int i = n / 2; i < n; i++) {
            back.add(Long.parseLong(st.nextToken()));
        }

        front = getSum(front);
        back = getSum(back);

        Collections.sort(front);

        long res = 0;
        HashMap<Long, Integer> frontCnt = new HashMap<>();
        HashMap<Long, Integer> backCnt = new HashMap<>();

        for (int i = 0; i < front.size(); i++) {
            long num = front.get(i);
            if (!frontCnt.containsKey(num))
                frontCnt.put(num, 0);
            frontCnt.put(num, frontCnt.get(num) + 1);
        }

        for (int i = 0; i < back.size(); i++) {
            long num = back.get(i);
            if (!backCnt.containsKey(num))
                backCnt.put(num, 0);
            backCnt.put(num, backCnt.get(num) + 1);
        }

        Collections.sort(back);

        for (Long f : frontCnt.keySet()) {
            long target = s - f;
            if (backCnt.containsKey(target))
                res += (long) backCnt.get(target) * frontCnt.get(f);
        }

        if (s == 0) res--;

        System.out.println(res);
    }
}