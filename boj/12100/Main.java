import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.BufferedWriter;
import java.io.OutputStreamWriter;
import java.io.IOException;
import java.util.Arrays;
import java.util.Queue;
import java.util.LinkedList;
import java.util.stream.Stream;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n = Integer.parseInt(br.readLine().replace(" ", ""));
        int[][] map = new int[n][n];
        for (int i = 0; i < n; i++) {
            map[i] = Stream.of(br.readLine().split(" "))
                        .mapToInt(Integer::parseInt)
                        .toArray();
        }
        // bw.write(Arrays.deepToString(map));
        bw.write(solve(n, map)+ "\n");
        br.close();
        bw.flush();
        bw.close();
    }
    static int solve(int n, int[][] map) {
        // int[][] directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
        int ret = max(map);
        Queue<int[][]> q = new LinkedList<int[][]>();
        q.add(map);
        for (int t = 0; t <= 5; t++) {
            int cnt = q.size();
            // System.out.println(cnt);
            for (int j = 0; j < cnt; j++) {
                map = q.poll();
                // System.out.println(Arrays.deepToString(map));
                ret = Math.max(ret, max(map));
                if (t >= 5) {
                    continue;
                }
                int[][] movedMap;
                boolean[][] mergedMap;

                mergedMap = new boolean[n][n];
                movedMap = copyMap(map);
                for (int y = 1; y < n; y++) {
                    for (int x = 0; x < n; x++) {
                        boolean merged = false;
                        for (int k = y; k > 0; k--) {
                            if (movedMap[k][x] == 0 || mergedMap[k-1][x]) {
                                break;
                            } else if (movedMap[k-1][x] == 0) {
                                movedMap[k-1][x] = movedMap[k][x];
                                movedMap[k][x] = 0;
                            } else if (movedMap[k][x] == movedMap[k-1][x] && !merged) {
                                movedMap[k-1][x] += movedMap[k][x];
                                movedMap[k][x] = 0;
                                mergedMap[k-1][x] = true;
                                merged = true;
                            } else {
                                break;
                            }
                        }
                    }
                }
                q.add(movedMap);

                mergedMap = new boolean[n][n];
                movedMap = copyMap(map);
                for (int y = n-2; y >= 0; y--) {
                    for (int x = 0; x < n; x++) {
                        boolean merged = false;
                        for (int k = y; k < n-1; k++) {
                            if (movedMap[k][x] == 0 || mergedMap[k+1][x]) {
                                break;
                            } else if (movedMap[k+1][x] == 0) {
                                movedMap[k+1][x] = movedMap[k][x];
                                movedMap[k][x] = 0;
                            } else if (movedMap[k][x] == movedMap[k+1][x] && !merged) {
                                movedMap[k+1][x] += movedMap[k][x];
                                movedMap[k][x] = 0;
                                mergedMap[k+1][x] = true;
                                merged = true;
                            } else {
                                break;
                            }
                        }
                    }
                }
                q.add(movedMap);

                mergedMap = new boolean[n][n];
                movedMap = copyMap(map);
                for (int y = 0; y < n; y++) {
                    for (int x = 1; x < n; x++) {
                        boolean merged = false;
                        for (int k = x; k > 0; k--) {
                            if (movedMap[y][k] == 0 || mergedMap[y][k-1]) {
                                break;
                            } else if (movedMap[y][k-1] == 0) {
                                movedMap[y][k-1] = movedMap[y][k];
                                movedMap[y][k] = 0;
                            } else if (movedMap[y][k] == movedMap[y][k-1] && !merged) {
                                movedMap[y][k-1] += movedMap[y][k];
                                movedMap[y][k] = 0;
                                mergedMap[y][k-1] = true;
                                merged = true;
                            } else {
                                break;
                            }
                        }
                    }
                }
                q.add(movedMap);

                mergedMap = new boolean[n][n];
                movedMap = copyMap(map);
                for (int y = 0; y < n; y++) {
                    for (int x = n-2; x >= 0; x--) {
                        boolean merged = false;
                        for (int k = x; k < n-1; k++) {
                            if (movedMap[y][k] == 0 || mergedMap[y][k+1]) {
                                break;
                            } else if (movedMap[y][k+1] == 0) {
                                movedMap[y][k+1] = movedMap[y][k];
                                movedMap[y][k] = 0;
                            } else if (movedMap[y][k] == movedMap[y][k+1] && !merged) {
                                movedMap[y][k+1] += movedMap[y][k];
                                movedMap[y][k] = 0;
                                mergedMap[y][k+1] = true;
                                merged = true;
                            } else {
                                break;
                            }
                        }
                    }
                }
                q.add(movedMap);
            }
        }
        return ret;
    }

    static int[][] copyMap(int[][] map) {
        int[][] copiedMap = new int[map.length][map[0].length];
        for (int i = 0; i < map.length; i++) {
            for (int j = 0; j < map[0].length; j++) {
                copiedMap[i][j] = map[i][j];
            }
        }
        return copiedMap;
    }
    static int max(int[][] map) {
        int ret = 0;
        for (int i = 0; i < map.length; i++) {
            for (int j = 0; j < map[0].length; j++) {
                if (map[i][j] > ret) {
                    ret = map[i][j];
                }
            }
        }
        return ret;
    }
}