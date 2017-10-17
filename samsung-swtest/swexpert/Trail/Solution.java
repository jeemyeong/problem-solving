import java.io.*;
import java.util.*;
import java.util.stream.*;


public class Solution {
    static boolean[][] visited;
    static int[][] Directions = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;

        int T = Integer.parseInt(br.readLine());
        for (int i = 0; i < T; i++) {
            st = new StringTokenizer(br.readLine());
            int N = Integer.parseInt(st.nextToken());
            int K = Integer.parseInt(st.nextToken());
            int[][] map = new int[N][N];
            visited = new boolean[N][N];
            for (int j = 0; j < N; j++) {
                map[j] = Stream.of(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
            }
            int ans = solve(N, K, map);
            bw.write("#" + (i+1) + " " +ans + "\n");
        }

        br.close();
        bw.flush();
        bw.close();

    } 
    static int solve(int N, int K, int[][] map) {
        int ans = 0;
        ArrayList<Point> maxList = findMax(N, map);
        for (Point point : maxList) {
            ans = Math.max(ans, dfs(N, K, map, map[point.y][point.x], point.y, point.x, false));
        }
        return ans;
    }

    static int dfs(int N, int K, int[][] map, int height, int y, int x, boolean shave) {
        int ret = 1;
        visited[y][x] = true;
        for (int[] d : Directions) {
            int dy = y + d[0];
            int dx = x + d[1];
            if (dy < 0 || dx < 0 || dy >= N || dx >= N || visited[dy][dx]) {
                continue;
            }
            
            if (map[dy][dx] < height) {
                ret = Math.max(ret, dfs(N, K, map, map[dy][dx], dy, dx, shave)+ 1);
            } else if (!shave && (map[dy][dx] - K) < map[y][x]) {
                ret = Math.max(ret, dfs(N, K, map, map[y][x]-1, dy, dx, true)+ 1);
            }
        }
        visited[y][x] = false;
        return ret;
    }

    
    static ArrayList<Point> findMax(int N, int[][] map) {
        ArrayList<Point> ret = new ArrayList<Point>();
        int max = 1;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (map[i][j] == max) {
                    ret.add(new Point(i, j));
                } else if (map[i][j] > max) {
                    max = map[i][j];
                    ret = new ArrayList<Point>();
                    ret.add(new Point(i, j));
                }
            }
        }
        return ret;
    }
    static class Point {
        int y, x;
        public Point(int y, int x) {
            this.y = y;
            this.x = x;
        }
    }
}