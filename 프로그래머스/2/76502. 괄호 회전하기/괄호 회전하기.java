import java.util.*;

class Solution {
    public int solution(String s) {
        int answer = 0;
        
        HashMap<Character, Character> pairs = new HashMap<>(){{
            put('[', ']');
            put('(', ')');
            put('{', '}');
        }};
        
        Set<Character> keys = pairs.keySet();
        
        ArrayDeque<Character> str = new ArrayDeque<>();
        for (char c : s.toCharArray()) {
            str.addLast(c);
        }
                
        A: for (int i = 0; i < s.length(); i++) {
            //System.out.println(i);
            //System.out.println(str);
            ArrayDeque<Character> dq = new ArrayDeque<>();
            for (Character c : str) {
                if (keys.contains(c)) { // 여는 괄호
                    dq.addLast(c); // 스택에넣음
                } else {
                    // 닫힌괄호
                    if (dq.isEmpty() || pairs.get(dq.pollLast()) != c) {
                        str.addLast(str.pollFirst()); // 회전
                        continue A;
                    }
                }
            }
            str.addLast(str.pollFirst()); // 회전
            
            if (dq.isEmpty()) answer++;
            //System.out.println(i + " = " + str.toString());
            
        }
        
        return answer;
    }
}