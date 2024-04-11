import java.util.*;

class Solution {
    boolean solution(String s) {
        boolean answer = true;
        ArrayDeque<Character> dq = new ArrayDeque<>();
        char[] arr = s.toCharArray();
        
        for (char c : arr) {
            if (c == '(') {
                dq.addLast(c);
            } else {
                // ')' 이면
                if (dq.isEmpty()) return false;
                dq.pollLast();
            }
        }
        
        if (!dq.isEmpty()) return false;

        return answer;
    }
}