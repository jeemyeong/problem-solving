import java.util.*;
import java.util.stream.*;
import java.io.*;

public class Film {
    static int[] rowOfZero;
    static int[] rowOfOne;
    static int[][] map;
    static int D;
    static int W;
    static int K;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;
        int T = Integer.parseInt(br.readLine());

        for (int i = 0; i < T; i++) {
            st = new StringTokenizer(br.readLine());
            D = Integer.parseInt(st.nextToken());
            W = Integer.parseInt(st.nextToken());
            K = Integer.parseInt(st.nextToken());
            rowOfZero = new int[W];
            rowOfOne = new int[W];
            for (int j = 0; j < W; j++) {
                rowOfOne[j] = 1;
            }
            map = new int[D][W];
            for (int j = 0; j < D; j++) {
                map[j] = Stream.of(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
            }
            int ans = solve(0);
            bw.write("#" + (i+1) + " " + ans +"\n");
            // System.out.println("#" + (i+1) + " " + ans);
        }
        bw.flush();
        br.close();
        bw.close();
    }

    static int solve(int row) {
        if (check()) {
            return 0;
        }

        if (row == D) {
            return D;
        }

        int ret = D;

        ret = Math.min(ret, solve(row+1));
        if (ret == 0) {
            return 0;
        }

        int[] origin = map[row];
        map[row] = rowOfZero;
        ret = Math.min(ret, solve(row+1)+1);
        if (ret == 1) {
            map[row] = origin;
            return 1;
        }

        map[row] = rowOfOne;
        ret = Math.min(ret, solve(row+1)+1);
        
        map[row] = origin;
        return ret;
    }
    static boolean check() {
        for (int j = 0; j < W; j++) {
            boolean pass = false;
            int last = -1;
            int count = 0;
            for (int i = 0; i < D; i++) {
                if (map[i][j] == last) {
                    count++;
                } else {
                    count = 1;
                    last = map[i][j];
                }
                if (count >= K) {
                    pass = true;
                    break;
                }
            }
            if (!pass) {
                return false;
            }
        }
        return true;
    }
}