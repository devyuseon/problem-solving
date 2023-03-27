import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.HashSet;

class TrieNode {

    public HashMap<Character, TrieNode> childNodes = new HashMap<>();
    public boolean isLaist;
}

class Trie {
    public TrieNode rootNode;

    Trie() {
        rootNode = new TrieNode();
    }

    void insert(String word) {
        TrieNode node = this.rootNode;

        for (char c : word.toCharArray()) {
            node = node.childNodes.computeIfAbsent(c, v -> new TrieNode());
        }
        node.isLaist = true;
    }

    boolean search(String word) {
        TrieNode node = this.rootNode;

        for (char c : word.toCharArray()) {
            if (!node.childNodes.containsKey(c)) return false;
            node = node.childNodes.get(c);
        }

        return node.isLaist;
    }
}

public class Main {

    public static Trie trie;
    public static char[][] board;
    public static boolean[][] visited;
    public static StringBuilder sb;
    public static HashSet<String> searched;
    public static int[] dx = {-1, 1, 0, 0, -1, -1, 1, 1};
    public static int[] dy = {0, 0, -1, 1, -1, 1, -1, 1};
    public static int[] score = {0, 0, 0, 1, 1, 2, 3, 5, 11};
    public static int maxScore = 0;
    public static String maxWord = "";

    public static void dfs(int x, int y) {
        if (trie.search(sb.toString())) {
            if (!searched.contains(sb.toString())) {
                searched.add(sb.toString()); // 찾은 목록에 추가
                maxScore += score[sb.toString().length()];
            }
            if (maxWord.length() <= sb.length()) {
                if (maxWord.length() == sb.length()) {
                    maxWord = (sb.toString().compareTo(maxWord) < 0) ? sb.toString() : maxWord;
                } else {
                    maxWord = sb.toString();
                }
            }
        }

        if (sb.length() == 8) return; // 단어는 최대 8글자

        for (int i = 0; i < 8; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];
            if (nx < 0 || nx >= 4 || ny < 0 || ny >= 4) continue;
            if (visited[nx][ny]) continue;

            visited[nx][ny] = true;
            sb.append(board[nx][ny]);
            dfs(nx, ny);
            visited[nx][ny] = false;
            sb.deleteCharAt(sb.length() - 1);
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int w = Integer.parseInt(br.readLine());
        trie = new Trie();
        StringBuilder res = new StringBuilder();

        // 사전 초기화
        for (int i = 0; i < w; i++) {
            trie.insert(br.readLine());
        }
        br.readLine();

        int b = Integer.parseInt(br.readLine());
        for (int t = 0; t < b; t++) {
            board = new char[4][4];
            visited = new boolean[4][4];
            sb = new StringBuilder();
            searched = new HashSet<>();
            maxScore = 0;
            maxWord = "";

            for (int i = 0; i < 4; i++) {
                board[i] = br.readLine().toCharArray();
            }

            for (int i = 0; i < 4; i++) {
                for (int j = 0; j < 4; j++) {
                    if (!trie.rootNode.childNodes.containsKey(board[i][j])) continue;
                    visited[i][j] = true;
                    sb.append(board[i][j]);
                    dfs(i, j);
                    visited[i][j] = false;
                    sb.setLength(0);
                }
            }

            if (searched.size() == 0) {
                res.append("0 0\n");
            } else {
                res.append(maxScore).append(" ").append(maxWord).append(" ").append(searched.size()).append("\n");
            }
            
            if (t < b - 1) br.readLine();
        }

        System.out.println(res);
    }
}