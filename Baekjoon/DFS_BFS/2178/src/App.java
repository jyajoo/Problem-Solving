import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class App {

    static int n, m;
    static int[][] board;
    static int[][] direction = { { -1, 0 }, { 1, 0 }, { 0, 1 }, { 0, -1 } };
    static boolean[][] visited;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        board = new int[n][m];
        visited = new boolean[n][m];

        for (int i = 0; i < n; i++) {
            String s = br.readLine();
            for (int j = 0; j < m; j++) {
                // String으로 저장된 문자열 중 하나씩 선택하여 char타입으로 변환
                // "1123" -> '1' -> 1
                board[i][j] = s.charAt(j) - '0';
            }
        }

        int result = Integer.MAX_VALUE;
        visited[0][0] = true;
        bfs(0, 0);

    }
    
    public static void bfs(int x, int y) {
        Queue<int[]> queue = new LinkedList<>();
        queue.add(new int[] { 1, 0, 0 });

        while(!queue.isEmpty()){
            int[] now = queue.poll();
            int cnt = now[0];
            int nowX = now[1];
            int nowY = now[2];

            if (nowX == n - 1 && nowY == m - 1){
                result
            }
        }
    }
}
