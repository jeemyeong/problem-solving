import java.util.*;
import java.util.stream.*;
import java.io.*;

public class Solution {
    static int[] rowOfZero;
    static int[] rowOfOne;
    static int[][] map;
    static int[][] temp;
    static int D;
    static int W;
    static int K;
    static int ans;
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
            temp = new int[D][W];
            for (int j = 0; j < D; j++) {
                temp[j] = Arrays.copyOf(map[j], W);
            }
            ans = D;
            solve(0, 0);
            bw.write("#" + (i+1) + " " + ans +"\n");
            // System.out.println("#" + (i+1) + " " + ans);
        }
        bw.flush();
        br.close();
        bw.close();
    }

    static void solve(int row, int cnt) {
        if (check()) {
            ans = Math.min(ans, cnt);
            return;
        }

        if (row == D || cnt > ans) {
            return;
        }
        solve(row+1, cnt);
        map[row] = rowOfZero;
        solve(row+1, cnt+1);
        map[row] = rowOfOne;
        solve(row+1, cnt+1);
        map[row] = temp[row];
        return;
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