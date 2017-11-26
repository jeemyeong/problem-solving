import java.io.*;
import java.util.*;
import java.util.stream.*;


public class Solution {
    Direction[] directions;
    public Solution() {
        directions = new Direction[4];
        directions[0] = new Direction(-1, 0);
        directions[1] = new Direction(1, 0);
        directions[2] = new Direction(0, -1);
        directions[3] = new Direction(0, 1);
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;

        int T = Integer.parseInt(br.readLine());
        for (int i = 0; i < T; i++) {
            String[] map = new String[8];
            for (int j = 0; j < 8; j++) {
                map[j] = br.readLine();
            }
            int ans = new Solution().solve(map);
            bw.write(ans + "\n");
        }
        br.close();
        bw.flush();
        bw.close();
    }
    int solve(String[] map) {
        int ans = 0;
        for (int i = 0; i < 8; i++) {
            for (int j = 0; j < 8; j++) {
                boolean[][] visited = new boolean[8][8];
                visited[i][j] = true;
                ans = Math.max(ans, this.dfs(i, j, map, visited, 1, false));
            }
        }
        return ans;
    }
    int dfs(int y, int x, String[] map, boolean[][] visited, int length, boolean connectedWithZ) {
        int ret = length;
        for (int i = 0; i < directions.length; i++) {
            int ny = y + directions[i].dy;
            int nx = x + directions[i].dx;
            if (ny < 0 || nx < 0 || ny >= 8 || nx >= 8) {
                continue;
            }
            if (visited[ny][nx]) {
                continue;
            }
            if (connect(map[y].charAt(x), map[ny].charAt(nx))) {
                visited[ny][nx] = true;
                ret = Math.max(ret, dfs(ny, nx, map, visited, length+1, connectedWithZ));
                visited[ny][nx] = false;
            } else if (!connectedWithZ && connectWithZ(map[y].charAt(x), map[ny].charAt(nx))) {
                visited[ny][nx] = true;
                ret = Math.max(ret, dfs(ny, nx, map, visited, length+1, true));
                visited[ny][nx] = false;
            }
        }
        return ret;
    }

    boolean connectWithZ(char a, char b) {
        if (a == 'Z' && b == 'A') {
            return true;
        }
        return false;
    }
    boolean connect(char a, char b) {
        if (a < b) {
            return true;
        }
        return false;
    }

    class Direction {
        int dy, dx;
        public Direction(int dy, int dx) {
            this.dy = dy;
            this.dx = dx;
        }
    }
}