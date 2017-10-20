import java.io.*;
import java.util.*;
import java.util.stream.*;


public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;

        int T = Integer.parseInt(br.readLine());
        for (int i = 0; i < T; i++) {
            st = new StringTokenizer(br.readLine());
            int N = Integer.parseInt(st.nextToken());
            int[][] map = new int[N][N];
            for (int j = 0; j < N; j++) {
                map[j] = Stream.of(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
            }
            int ans = solve(N, map);
            bw.write("#" + (i+1) + " " + ans + "\n");
        }
        br.close();
        bw.flush();
        bw.close();
    }
    static int solve(int N, int[][] map) {
        ArrayList<Point> points = new ArrayList<Point>();
        ArrayList<Point> stairs = new ArrayList<Point>();
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (map[i][j] == 1) {
                    points.add(new Point(i, j));
                } else if (map[i][j] != 0) {
                    stairs.add(new Point(i, j));
                }
            }
        }

        int size = points.size();
        Queue<Integer> q = new LinkedList<Integer>();
        q.add(0);
        q.add(1);
        for (int i = 1; i < size; i++) {
            int qSize = q.size();
            for (int j = 0; j < qSize; j++) {
                Integer cur = q.poll();
                q.add(cur*2);
                q.add(cur*2+1);
            }
        }
        int ans = 100000000;
        while (!q.isEmpty()) {
            Integer caseInfo = q.poll();
            ans = Math.min(ans, simulate(N, map, points, stairs, caseInfo, ans));
        }
        return ans;
    }

    static int simulate(int N, int[][] map, ArrayList<Point> points, ArrayList<Point> stairs, int caseInfo, int ans) {
        
        ArrayList<Point> stair1 = new ArrayList<Point>();
        ArrayList<Point> stair2 = new ArrayList<Point>();

        ArrayList<Point> goingToStair1 = new ArrayList<Point>();
        ArrayList<Point> goingToStair2 = new ArrayList<Point>();

        Queue<Point> waitingToStair1 = new LinkedList<Point>();
        Queue<Point> waitingToStair2 = new LinkedList<Point>();
        for (int i = 0; i < points.size(); i++) {
            points.get(i).waiting = 0;
            if (caseInfo%2 == 0) {
                goingToStair1.add(points.get(i));
            } else {
                goingToStair2.add(points.get(i));
            }
            caseInfo /= 2;
        }
        for (int t = 1; true; t++) {
            for (int i = 0; i < goingToStair1.size(); i++) {
                Point point = goingToStair1.get(i);
                if (t > (Math.abs(point.y-stairs.get(0).y) + Math.abs(point.x-stairs.get(0).x))) {
                    waitingToStair1.add(point);
                    goingToStair1.remove(i);
                    i--;
                }
            }
            for (int i = 0; i < goingToStair2.size(); i++) {
                Point point = goingToStair2.get(i);
                if (t > (Math.abs(point.y-stairs.get(1).y) + Math.abs(point.x-stairs.get(1).x))) {
                    waitingToStair2.add(point);
                    goingToStair2.remove(i);
                    i--;
                }
            }

            for (int i = 0; i < stair1.size(); i++) {
                stair1.get(i).waiting++;
                if (stair1.get(i).waiting == map[stairs.get(0).y][stairs.get(0).x]) {
                    stair1.remove(i);
                    i--;
                }
            }
            for (int i = 0; i < stair2.size(); i++) {
                stair2.get(i).waiting++;
                if (stair2.get(i).waiting == map[stairs.get(1).y][stairs.get(1).x]) {
                    stair2.remove(i);
                    i--;
                }
            }
            while (stair1.size() < 3 && waitingToStair1.size() > 0) {
                stair1.add(waitingToStair1.poll());
            }
            while (stair2.size() < 3 && waitingToStair2.size() > 0) {
                stair2.add(waitingToStair2.poll());
            }
            
            if (stair1.size() == 0 && goingToStair1.size() == 0 && waitingToStair1.size() == 0 && stair2.size() == 0 && goingToStair2.size() == 0 && waitingToStair2.size() == 0) {
                return t;
            }
            if (t > ans) {
                return t;
            }
        }
    }

    static class Point {
        int y,x;
        int waiting = 0;
        public Point(int y, int x) {
            this.y = y;
            this.x = x;
        }
        @Override
        public String toString() {
            return "Y: " + y + " X: " + x + " waiting: " + waiting; 
        }
    }
}