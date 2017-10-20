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
            int M = Integer.parseInt(st.nextToken());
            int K = Integer.parseInt(st.nextToken());
            Microbe[][] map = new Microbe[N][N];
            for (int j = 0; j < K; j++) {
                st = new StringTokenizer(br.readLine());
                int y = Integer.parseInt(st.nextToken());
                int x = Integer.parseInt(st.nextToken());
                int count = Integer.parseInt(st.nextToken());
                int direction = Integer.parseInt(st.nextToken());
                map[y][x] = new Microbe(count, direction);
            }
            int ans = solve(N, M, map);
            bw.write("#" + (i+1) + " " + ans + "\n");
        }
        br.close();
        bw.flush();
        bw.close();
    }
    static int solve(int N, int M, Microbe[][] map) {
        for (int i = 0; i < M; i++) {
            map = oneHourPass(N, map);
        }
        int ans = 0;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (map[i][j] == null) {
                    continue;
                }
                ans += map[i][j].count;
            }
        }
        return ans;
    }
    static Microbe[][] oneHourPass (int N, Microbe[][] map) {
        int[][] direction = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
        Microbe[][] ret = new Microbe[N][N];
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (map[i][j] == null) {
                    continue;
                }
                map[i][j].directionWeight = map[i][j].count;
                int[] d = direction[map[i][j].direction-1];
                int dy = i+d[0];
                int dx = j+d[1];
                if (ret[dy][dx] == null) {
                    ret[dy][dx] = map[i][j];
                } else {
                    ret[dy][dx] = ret[dy][dx].mergeMicrobe(map[i][j]);
                }
                if (dy == 0 || dy == N-1 || dx == 0 || dx == N-1) {
                    ret[dy][dx].changeDirection();
                    if (ret[dy][dx].divideCount() == 0) {
                        ret[dy][dx] = null;
                        continue;
                    }
                }
            }
        }
        return ret;
    }
    static class Microbe{
        int count, direction, directionWeight;
        public Microbe(int count, int direction) {
            this.count = count;
            this.direction = direction;
            this.directionWeight = count;
        }
        void changeDirection() {
            switch(this.direction) {
                case 1:
                    this.direction = 2;
                    break;
                case 2:
                    this.direction = 1;
                    break;
                case 3:
                    this.direction = 4;
                    break;
                case 4:
                    this.direction = 3;
                    break;
                default:
                    break;
            }
        }
        int divideCount() {
            this.count /=  2;
            return this.count;
        }
        Microbe mergeMicrobe(Microbe microbeToMerge) {
            if (this.directionWeight > microbeToMerge.directionWeight) {
                this.count += microbeToMerge.count;
                return this;
            } else {
                microbeToMerge.count += this.count;
                return microbeToMerge;
            }
        }
        @Override
        public String toString() {
            return this.count + " " + this.direction + " " + this.directionWeight;
        }
    }
}