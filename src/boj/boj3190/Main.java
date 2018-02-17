package boj.boj3190;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;
import java.util.Arrays;
import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;
        int N = Integer.parseInt(br.readLine());
        int K = Integer.parseInt(br.readLine());
        boolean[][] apples = new boolean[N+1][N+1];
        for (int i = 0; i < K; i++) {
            st = new StringTokenizer(br.readLine());
            int y = Integer.parseInt(st.nextToken());
            int x = Integer.parseInt(st.nextToken());
            apples[y][x] = true;
        }
        int L = Integer.parseInt(br.readLine());
        char[] directions = new char[10001];
        for (int i = 0; i < L; i++) {
            st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            char c = st.nextToken().charAt(0);
            directions[x] = c;
        }
        // System.out.println(Arrays.toString(directions));
        bw.write(solve(N, K, L, apples, directions)+ "\n");
        br.close();
        bw.flush();
        bw.close();
    }
    static int solve(int N, int K, int L, boolean[][] apples, char[] directions) {
        boolean[][] map = new boolean[N+1][N+1];
        List<Point> q = new ArrayList<Point>();
        q.add(new Point(1, 1));
        map[1][1] = true;
        Direction d = new Direction(0, 1);
        int i = 0;
        while (true) {
            i++;
            Point head = q.get(0);
            Point new_head = new Point(head.y+d.y, head.x+d.x);
            if (new_head.y <= 0 || new_head.x <= 0 || new_head.y > N || new_head.x > N) {
                return i;
            }
            if (map[new_head.y][new_head.x]) {
                return i;
            }
            q.add(0, new_head);
            map[new_head.y][new_head.x] = true;
            if (!apples[new_head.y][new_head.x]) {
                Point tail = q.get(q.size()-1);
                q.remove(q.size()-1);
                map[tail.y][tail.x] = false;
            } else {
                apples[new_head.y][new_head.x] = false;
            }
            if (directions[i] == 'D') {
                int temp = d.y;
                d.y = d.x;
                d.x = temp * (-1);
            } else if (directions[i] == 'L') {
                int temp = d.y;
                d.y = d.x * (-1);
                d.x = temp;
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
        public Direction(int y, int x) {
            this.y = y;
            this.x = x;
        }
    }
}