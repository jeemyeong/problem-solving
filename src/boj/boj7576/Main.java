package boj.boj7576;

import java.io.IOException;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;
import java.util.Queue;
import java.util.LinkedList;
import java.util.Arrays;
import java.util.stream.Stream;


public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        int m = Integer.parseInt(st.nextToken());
        int n = Integer.parseInt(st.nextToken());
        int[][] map = new int[n][m];
        for (int i = 0; i < n; i++) {
            map[i] = Stream.of(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        }

        bw.write(solve(n, m, map) + "\n");

        br.close();
        bw.flush();
        bw.close();
    } 
    static int solve(int n, int m, int[][] map) {
        Queue<Point> q = new LinkedList<Point>();
        int[][] directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
        boolean ripen = false;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (map[i][j] == 1) {
                    q.add(new Point(i, j));
                } else if (map[i][j] == 0) {
                    ripen = true;
                }
            }
        }
        if (!ripen) {
            return 0;
        }

        boolean[][] visited = new boolean[n][m];
        int days = 0;
        while (!q.isEmpty()) {
            int size = q.size();
            for (int i = 0; i < size; i++) {
                Point cur = q.poll();
                if (visited[cur.y][cur.x] || map[cur.y][cur.x] == -1) {
                    continue;
                }
                visited[cur.y][cur.x] = true;
                map[cur.y][cur.x] = days;
                for (int[] d : directions) {
                    int dy = cur.y + d[0];
                    int dx = cur.x + d[1];
                    if (dy < 0 || dx < 0 || dy >= n || dx >= m) {
                        continue;
                    }
                    q.add(new Point(dy, dx));
                }
            }
            days++;
        }
        int ans = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (map[i][j] > ans) {
                    ans = map[i][j];
                } else if (map[i][j] == 0 && !visited[i][j]) {
                    return -1;
                }
            }
        }
        return ans;
    }
    static class Point {
        int y, x;
        public Point(int y, int x) {
            this.y = y;
            this.x = x;
        }
    }
}