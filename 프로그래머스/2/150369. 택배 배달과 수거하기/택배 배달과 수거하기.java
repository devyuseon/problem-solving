import java.util.Arrays;
import java.util.HashMap;

class Solution {
    public static long solution(int cap, int n, int[] deliveries, int[] pickups) {
        long answer = 0;

        HashMap<Integer, Integer> dMemo = new HashMap<>();
        HashMap<Integer, Integer> pMemo = new HashMap<>();

        dMemo.put(deliveries[0], 0);
        pMemo.put(pickups[0], 0);

        for (int i = 1; i < n; i++) {
            deliveries[i] += deliveries[i - 1];
            if (!dMemo.containsKey(deliveries[i])) {
                dMemo.put(deliveries[i], i);
            }
            pickups[i] += pickups[i - 1];
            if (!pMemo.containsKey(pickups[i])) {
                pMemo.put(pickups[i], i);
            }
        }

        int d = deliveries[n - 1];
        int p = pickups[n - 1];

        while (d > 0 || p > 0) {
            int dSearch = getIndex(deliveries, d, dMemo);
            int pSearch = getIndex(pickups, p, pMemo);
            int max = Math.max(dSearch, pSearch);
            answer += (max + 1) * 2;
            d -= cap;
            p -= cap;
        }

        return answer;
    }

    public static int getIndex(int[] array, int target, HashMap<Integer, Integer> memo) {
        if (memo.containsKey(target)) {
            return memo.get(target);
        } else {
            int index = Arrays.binarySearch(array, target);
            return index * (-1) - 1;
        }
    }
}