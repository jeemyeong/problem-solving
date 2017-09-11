import java.util.Queue;
import java.util.LinkedList;

class ColoringBook {
    public static void main(String[] args) {
        ColoringBook book = new ColoringBook();
        int m = 6;
        int n = 4;
        int[][] picture = {{1, 1, 1, 0}, {1, 2, 2, 0}, {1, 0, 0, 1}, {0, 0, 0, 1}, {0, 0, 0, 3}, {0, 0, 0, 3}};
        int[] ret = book.solution(m, n, picture);
        System.out.println(ret[0]);
        System.out.println(ret[1]);
    }
    public int[] solution(int m, int n, int[][] picture) {
        int numberOfArea = 0;
        int maxSizeOfOneArea = 0;
        boolean[][] visited = new boolean[m][n];
        Queue<Point> q = new LinkedList<Point>();
        int[][] directions = {{1,0}, {-1,0}, {0,1}, {0,-1}};
        q.offer(new Point(0, 0));
        while (!q.isEmpty()) {
            Queue<Point> eachQ = new LinkedList<Point>();
            Point newCur = q.poll();
            if (visited[newCur.y][newCur.x]) {
                continue;
            }
            int sizeOfOneArea = 0;
            eachQ.offer(newCur);
            while(!eachQ.isEmpty()) {
                Point cur = eachQ.poll();
                if (visited[cur.y][cur.x]) {
                    continue;
                }
                sizeOfOneArea++;
                visited[cur.y][cur.x] = true;
                int color = picture[cur.y][cur.x];
                for (int[] direction : directions) {
                    int dy = cur.y + direction[0];
                    int dx = cur.x + direction[1];
                    if (dy < 0 || dy >= m || dx < 0 || dx >= n || visited[dy][dx]) {
                        continue;
                    }
                    if (picture[dy][dx] == picture[cur.y][cur.x]) {
                        eachQ.offer(new Point(dy, dx));
                    } else {
                        q.offer(new Point(dy, dx));
                    }
                    visited[dy][dx] = true;
                }
            }
            if (picture[newCur.y][newCur.x] != 0) {
                numberOfArea ++;
                maxSizeOfOneArea = Math.max(maxSizeOfOneArea, sizeOfOneArea);
            }
        }

        int[] answer = new int[2];
        answer[0] = numberOfArea;
        answer[1] = maxSizeOfOneArea;
        return answer;
    }
}

class Point{
    public int y, x;
    public Point(int y, int x) {
        this.y = y;
        this.x = x;
    }
}