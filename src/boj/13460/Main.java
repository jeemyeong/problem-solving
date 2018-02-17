import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.IOException;
import java.util.StringTokenizer;
import java.util.Queue;
import java.util.LinkedList;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;
        st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        char[][] map = new char[n][m];
        for (int i = 0; i < n; i++) {
            map[i] = br.readLine().toCharArray();
        }
        bw.write(solve(n, m, map) + "\n");
        br.close();
        bw.flush();
        bw.close();
    }
    static int solve(int n, int m, char[][] map) {
        int[][] directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
        Point red = null;
        Point blue = null;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (map[i][j] == 'R') {
                    map[i][j] = '.';
                    red = new Point(i, j);
                } else if (map[i][j] == 'B') {
                    map[i][j] = '.';
                    blue = new Point(i, j);
                }
            }
        }
        Queue<Pair> q = new LinkedList<Pair>();
        q.add(new Pair(red, blue));
        boolean[][][][] visited = new boolean[n][m][n][m];
        for (int t = 0; t < 10; t++) {
            int cnt = q.size();
            for (int i = 0; i < cnt; i++) {
                Pair cur = q.poll();
                red = cur.red;
                blue = cur.blue;
                if (visited[cur.red.y][cur.red.x][cur.blue.y][cur.blue.x]) {
                    continue;
                }
                visited[cur.red.y][cur.red.x][cur.blue.y][cur.blue.x] = true;
                for (int[] direction : directions) {
                    Point moved_red = move(new Point(red), new Point(blue), direction, map);
                    Point moved_blue = move(new Point(blue), new Point(moved_red), direction, map);
                    moved_red = move(new Point(moved_red), new Point(moved_blue), direction, map);
                    if (moved_blue.y == -1) {
                        continue;
                    }
                    if (moved_red.y == -1) {
                        return t+1;
                    }
                    q.add(new Pair(moved_red, moved_blue));
                }
            }
        }
        return -1;
    }
    static Point move(Point runner, Point opposite, int[] direction, char[][] map) {
        while (true) {
            if (runner.y == -1 || runner.x == -1) {
                return runner;
            }
            if ((runner.y+direction[0]) == opposite.y && (runner.x+direction[1]) == opposite.x) {
                return runner;
            }
            if (map[runner.y+direction[0]][runner.x+direction[1]] == '#') {
                return runner;
            }
            if (map[runner.y+direction[0]][runner.x+direction[1]] == 'O') {
                runner.y = -1;
                runner.x = -1;
                return runner;
            }
            if (map[runner.y+direction[0]][runner.x+direction[1]] == '.') {
                runner.y += direction[0];
                runner.x += direction[1];
            }
        }
    }
    static class Point {
        public int y, x;
        public Point(int y, int x) {
            this.y = y;
            this.x = x;
        }
        public Point(Point original) {
            this.y = original.y;
            this.x = original.x;
        }
        public void print() {
            System.out.print("y: ");
            System.out.print(y);
            System.out.print(", x: ");
            System.out.print(x);
            System.out.println();
        }
    }
    static class Pair {
        public Point red, blue;
        public Pair(Point red, Point blue) {
            this.red = red;
            this.blue = blue;
        }
        public void print() {
            System.out.print("red: ");            
            red.print();
            System.out.print("blue: ");            
            blue.print();
            System.out.println();
        }
    }
}