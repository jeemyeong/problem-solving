package boj.boj14503;

import java.io.IOException;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;
import java.util.stream.Stream;
import java.util.Stack;


public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(br.readLine());
        int r = Integer.parseInt(st.nextToken());
        int c = Integer.parseInt(st.nextToken());
        int d = Integer.parseInt(st.nextToken());
        int[][] map = new int[n][m];
        for (int i = 0; i < n; i++) {
            map[i] = Stream.of(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        }
        bw.write(solve(n, m, r, c, d, map) + "\n");

        br.close();
        bw.flush();
        bw.close();

    } 
    static int solve(int n, int m, int r, int c, int d, int[][] map) {
        Point cur = new Point(r, c);
        Direction dir = new Direction(d);
        int[][] cleaned = new int[n][m];
        int ret = 0;
        int cnt = 0;
        while (true) {
            cnt++;
            if (cleaned[cur.y][cur.x] == 0) {
                cleaned[cur.y][cur.x] = 1;
                ret++;
            }
            boolean find = false;
            for (int i = 0; i < 4; i++) {
                dir.turnLeft();
                Point nextPoint = new Point(cur.y+dir.y, cur.x+dir.x);
                
                if (nextPoint.y < 0 || nextPoint.x < 0 || nextPoint.y >= n || nextPoint.x >= m) {
                    continue;
                }
                if (map[nextPoint.y][nextPoint.x] == 0 && cleaned[nextPoint.y][nextPoint.x] == 0) {
                    cur = nextPoint;
                    find = true;
                    break;
                }
            }
            if (!find) {
                if (map[cur.y-dir.y][cur.x-dir.x] == 1) {
                    return ret;
                } else {
                    cur.y = cur.y-dir.y;
                    cur.x = cur.x-dir.x;
                }
            }
        }
    }
    static class Point {
        int y, x;
        public Point(int y, int x) {
            this.y = y;
            this.x = x;
        }
    }
    static class Direction {
        int y, x;
        public Direction(int d) {
            switch (d) {
                case 0:
                    this.y = -1;
                    this.x = 0;
                    break;
                case 1:
                    this.y = 0;
                    this.x = 1;                
                    break;
                case 2:
                    this.y = 1;
                    this.x = 0;
                    break;
                case 3:
                    this.y = 0;
                    this.x = -1;                
                    break;
                default:
                    break;
            }
        }
        public Direction(int y, int x) {
            this.y = y;
            this.x = x;
        }
        public void turnLeft() {
            int temp = this.y;
            this.y = this.x * (-1);
            this.x = temp;
        }
    }
}