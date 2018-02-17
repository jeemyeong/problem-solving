package boj.boj14500;

import java.io.IOException;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;
import java.util.stream.Stream;


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
    static int solve(int n, int m, int[][] map)  {
        int[][][] directions = {
            {{0, 0}, {0, 1}, {0, 2}, {0, 3}},
            {{0, 0}, {0, 1}, {1, 0}, {1, 1}}, 
            {{0, 0}, {1, 0}, {2, 0}, {3, 0}},
            {{0, 0}, {0, 1}, {0, 2}, {1, 2}}, 
            {{0, 0}, {1, 0}, {2, 0}, {2, 1}}, 
            {{0, 1}, {1, 1}, {2, 1}, {2, 0}},
            {{0, 0}, {0, 1}, {0, 2}, {1, 0}},
            {{0, 2}, {1, 0}, {1, 1}, {1, 2}},
            {{0, 0}, {0, 1}, {1, 1}, {2, 1}},
            {{0, 0}, {1, 0}, {1, 1}, {1, 2}},
            {{0, 1}, {0, 2}, {1, 0}, {1, 1}},
            {{0, 0}, {0, 1}, {1, 1}, {1, 2}},
            {{0, 1}, {1, 0}, {1, 1}, {2, 0}},
            {{0, 0}, {1, 0}, {1, 1}, {2, 1}},
            {{0, 0}, {1, 0}, {2, 0}, {0, 1}},
            {{0, 0}, {0, 1}, {0, 2}, {1, 1}},
            {{0, 0}, {1, 0}, {2, 0}, {1, 1}},
            {{0, 1}, {1, 0}, {2, 1}, {1, 1}},
            {{0, 1}, {1, 0}, {1, 1}, {1, 2}}
        };
        int ret = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                for (int[][] direction : directions) {
                    ret = Math.max(ret, sumOfFourElements(n, m, direction, i, j, map));
                    // System.out.println(sumOfFourElements(n, m, direction, i, j, map));
                }
            }
        }
        return ret;
    }

    static int sumOfFourElements(int n, int m, int[][] direction, int y, int x, int[][] map) {
        int ret = 0;
        for (int i = 0; i < 4; i++) {
            int dy = y + direction[i][0];
            int dx = x + direction[i][1];
            if (dy < 0 || dx < 0 || dy >= n || dx >= m) {
                return 0;
            }
            ret += map[dy][dx];
        }
        return ret;
    }
}