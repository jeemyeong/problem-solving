import java.io.IOException;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;
import java.util.stream.Stream;
import java.util.ArrayList;
import java.util.Queue;
import java.util.LinkedList;
import java.util.PriorityQueue;
import java.util.Comparator;
import java.util.Arrays;

public class Main {
    public static int INF = 987654321;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;
        
        int t = Integer.parseInt(br.readLine());
        int y, x;
        for (int i = 0; i < t; i++) {
            int j = Integer.parseInt(br.readLine());
            st = new StringTokenizer(br.readLine());
            x = Integer.parseInt(st.nextToken());
            y = Integer.parseInt(st.nextToken());
            Point from = new Point(y, x);
            st = new StringTokenizer(br.readLine());
            x = Integer.parseInt(st.nextToken());
            y = Integer.parseInt(st.nextToken());
            Point to = new Point(y, x);
            int n = Integer.parseInt(br.readLine());
            Point[] points = new Point[n+2];
            points[0] = from;
            points[1] = to;
            for (int k = 2; k < n+2; k++) {
                st = new StringTokenizer(br.readLine());
                x = Integer.parseInt(st.nextToken());
                y = Integer.parseInt(st.nextToken());
                Point p = new Point(y, x);
                points[k] = p;
            }
            bw.write(solve(j, from, to, n, points)+'\n');
        }

        br.close();
        bw.flush();
        bw.close();
    }
    public static String solve(int j, Point from, Point to, int n, Point[] points) {
        for (int i = 0; i < points.length; i++) {
            for (int k = i+1; k < points.length; k++) {
                int d = (int) (Math.pow((points[i].y - points[k].y) ,2) + Math.pow((points[i].x - points[k].x) ,2));
                if (d <= (j * j)) {
                    points[k].addEdge(points[i]);
                    points[i].addEdge(points[k]);
                }
            }
        }
        boolean[][] visited = new boolean[2001][2001];
        if (from.edges.isEmpty() || to.edges.isEmpty()) {
            return "NO";
        }
        PriorityQueue<Point> q = new PriorityQueue<Point>(new Comparator<Point>(){
            @Override
            public int compare(Point p1, Point p2) {
                return p1.d - p2.d;
            }
        });
        // Queue<Point> q = new LinkedList<Point>();
        q.add(from);
        while (!q.isEmpty()) {
            Point cur = q.poll();
            // cur.print();
            if (cur == to) {
                return "YES";
            }
            if (visited[cur.y+1000][cur.x+1000]) {
                continue;
            }
            visited[cur.y+1000][cur.x+1000] = true;
            for (Point next : cur.edges) {
                next.d = cur.d + (int) (Math.pow((next.y - cur.y) ,2) + Math.pow((next.x - cur.x) ,2));
                q.add(next);
            }
        }
        return "NO";
    }
    static class Point {
        public int y, x, d;
        public ArrayList<Point> edges;
        public Point(int y, int x) {
            this.y = y;
            this.x = x;
            this.d = 0;
            this.edges = new ArrayList<Point>();
        }
        public void addEdge(Point point) {
            this.edges.add(point);
        }
        public void print() {
            System.out.print("y: ");
            System.out.print(y);
            System.out.print(", x: ");
            System.out.print(x);
            System.out.print(", d: ");
            System.out.print(d);
            System.out.println();
        }
        public void printEdge() {
            for (Point edge : edges) {
                edge.print();
            }
        }
    }
}