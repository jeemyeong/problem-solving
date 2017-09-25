import java.io.IOException;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;


public class CloestPair {
    public static int INF = 987654321;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;

        int n = Integer.parseInt(br.readLine());
        ArrayList<Point> points = new ArrayList<Point>();
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            points.add(new Point(x, y));
        }
        Collections.sort(points, new Comparator<Point>() {
            @Override
            public int compare(Point point1, Point point2) {
                return point1.x - point2.x;
            }
        });
        bw.write(solve(points, 0, n-1) + "\n");

        br.close();
        bw.flush();
        bw.close();
    } 

    public static int solve(ArrayList<Point> points, int start, int end) {
        if (start == end) {
            return INF;
        }
        int mid = (start+end)/2;
        int d = Math.min(solve(points, start, mid), solve(points, mid+1, end));
        int i = mid;
        while (i <= end && (int)Math.pow((points.get(mid).x - points.get(i).x), 2) < d) {
            i ++;
        }
        int j = mid;
        while (j >= start && (int)Math.pow((points.get(mid).x - points.get(j).x), 2) < d) {
            j --;
        }
        ArrayList<Point> center = new ArrayList<Point>();
        for (int k = j+1; k < i; k++) {
            center.add(points.get(k));
        }
        Collections.sort(center, new Comparator<Point>() {
            @Override
            public int compare(Point point1, Point point2) {
                return point1.y - point2.y;
            }
        });
        int centerSize = center.size();
        for (i = 0; i < centerSize-1; i++) {
            for (j = i+1; j < i+6; j++) {
                if (j >= centerSize) {
                    break;
                }
                d = Math.min(d, dist(center.get(i), center.get(j)));
            }
        }
        return d;
    }

    public static int dist(Point point1, Point point2) {
        return (int) Math.pow((point1.x-point2.x), 2) + (int) Math.pow((point1.y-point2.y), 2);
    }
}

class Point {
    public int x, y;
    Point(int x, int y) {
        this.x = x;
        this.y = y;
    }
}