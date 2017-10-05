import java.io.IOException;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;
import java.util.stream.Stream;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
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
        int[][] directions = {{-1, 0}, {1, 0}, {0, 1}, {0, -1}};
        List<Position> allEmpty = new ArrayList<Position>();
        List<Position> allFire = new ArrayList<Position>();
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (map[i][j] == 0) {
                    allEmpty.add(new Position(i, j));
                } else if (map[i][j] == 2) {
                    allFire.add(new Position(i, j));
                }
            }
        }
        int emptySize = allEmpty.size();
        List<List<Position>> emptyCombinations = new ArrayList<List<Position>>();
        for (int i = 0; i < emptySize-2; i++) {
            Position firstEmpty = allEmpty.get(i);
            for (int j = i+1; j < emptySize-1; j++) {
                Position secondEmpty = allEmpty.get(j);
                for (int k = j+1; k < emptySize; k++) {
                    Position thirdEmpty = allEmpty.get(k);
                    List<Position> emptyCombination = new ArrayList<Position>();
                    emptyCombination.add(firstEmpty);
                    emptyCombination.add(secondEmpty);
                    emptyCombination.add(thirdEmpty);
                    emptyCombinations.add(emptyCombination);
                }
            }
        }
        int ret = 0;
        for (List<Position> emptyCombination : emptyCombinations) {
            int[][] copiedMap = copyMap(n, m, map);
            for (Position empty : emptyCombination) {
                copiedMap[empty.y][empty.x] = 1;
            }
            int[][] visitedFire = new int[n][m];
            for (Position fire : allFire) {
                Queue<Position> q = new LinkedList<Position>();
                q.add(fire);
                while (!q.isEmpty()) {
                    Position cur = q.poll();
                    if (visitedFire[cur.y][cur.x] == 1) {
                        continue;
                    }
                    visitedFire[cur.y][cur.x] = 1;
                    copiedMap[cur.y][cur.x] = 2;
                    for (int[] direction : directions) {
                        Position nextPosition = new Position(cur.y+direction[0], cur.x+direction[1]);
                        if (nextPosition.y < 0 || nextPosition.x < 0 || nextPosition.y >= n || nextPosition.x >= m) {
                            continue;
                        }
                        if (copiedMap[nextPosition.y][nextPosition.x] == 0) {
                            q.add(nextPosition);
                        }
                    }
                }
            }
            ret = Math.max(ret, count(n, m, copiedMap));
        }
        return ret;
    }
    static int count(int n, int m, int[][] map) {
        int ret = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (map[i][j] == 0) {
                    ret += 1;
                }
            }
        }
        return ret;
    }
    static int[][] copyMap(int n, int m, int[][] map) {
        int[][] copiedMap = new int[n][m];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                copiedMap[i][j] = map[i][j];
            }
        }
        return copiedMap;
    }
    static class Position {
        int y, x;
        public Position(int y, int x) {
            this.y = y;
            this.x = x;
        }
    }
}   