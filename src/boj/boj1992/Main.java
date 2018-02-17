package boj.boj1992;

import java.io.IOException;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;
import java.util.stream.Stream;

public class Main {
    public static int INF = 987654321;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        
        int n = Integer.parseInt(br.readLine());
        int[][] map = new int[n][n];
        for (int i = 0; i < n; i++) {
            map[i] = Stream.of(br.readLine().split(""))
                .mapToInt(Integer::parseInt)
                .toArray();
        }

        bw.write(solve(n, map, new Pair(0, 0), new Pair(n-1, n-1))+'\n');

        br.close();
        bw.flush();
        bw.close();
    }
    public static String solve(int n, int[][] map, Pair from, Pair to) {
        if (from.y == to.y && from.x == to.x) {
            return Integer.toString(map[from.y][from.x]);
        }
        int mid_y = (from.y + to.y) / 2;
        int mid_x = (from.x + to.x) / 2;
        String s1 = solve(n, map, new Pair(from.y, from.x) , new Pair(mid_y, mid_x));
        String s2 = solve(n, map, new Pair(from.y, mid_x+1) , new Pair(mid_y, to.x));
        String s3 = solve(n, map, new Pair(mid_y+1, from.x) , new Pair(to.y, mid_x));
        String s4 = solve(n, map, new Pair(mid_y+1, mid_x+1) , new Pair(to.y, to.x));
        if (s1.equals("0") && s2.equals("0") && s3.equals("0") && s4.equals("0")) {
            return "0";
        }
        if (s1.equals("1") && s2.equals("1") && s3.equals("1") && s4.equals("1")) {
            return "1";
        }
        return "("+s1+s2+s3+s4+")";
    }
    static class Pair {
        public int y, x;
        public Pair(int y, int x) {
            this.y = y;
            this.x = x;
        }
    }
}