import java.util.*;

class Solution {
    public int solution(int[] topping) {
        int res = 0;
        HashMap<Integer, Integer> toppingCnt1 = new HashMap<>();
        HashMap<Integer, Integer> toppingCnt2 = new HashMap<>();
        for (int t : topping) {
            if (!toppingCnt1.containsKey(t))
                toppingCnt1.put(t, 0);
            toppingCnt1.put(t, toppingCnt1.get(t) + 1);
        }

        for (int i = 1; i < topping.length; i++) {
            // 앞에서 하나 빼고
            toppingCnt1.put(topping[i - 1], toppingCnt1.get(topping[i - 1]) - 1);
            // 뒤에 넣고
            if (!toppingCnt2.containsKey(topping[i - 1]))
                toppingCnt2.put(topping[i - 1], 0);
            toppingCnt2.put(topping[i - 1], toppingCnt2.get(topping[i - 1]));
            // 앞에서 뺀거 처리
            if (toppingCnt1.get(topping[i - 1]) == 0)
                toppingCnt1.remove(topping[i - 1]);
            
            if (toppingCnt1.keySet().size() == toppingCnt2.keySet().size())
                res++;
            
        }
        return res;
    }
}