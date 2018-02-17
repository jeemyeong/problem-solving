import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;
import java.util.Arrays;
import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;
        st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int y = Integer.parseInt(st.nextToken());
        int x = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());
        int[][] map = new int[N][M];
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < M; j++) {
                map[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        st = new StringTokenizer(br.readLine());
        int[] orders = new int[K];
        for (int i = 0; i < K; i++) {
            orders[i] = Integer.parseInt(st.nextToken());
        }
        bw.write(solve(N, M, y, x, K, map, orders));
        br.close();
        bw.flush();
        bw.close();
    }
    static String solve(int N, int M, int y, int x, int K, int[][] map, int[] orders) {
        String ret = "";
        int[][] dice = new int[4][3];
        dice[3][1] = map[y][x];
        for (int i = 0; i < K; i++) {
            int order = orders[i];
            switch (order) {
                case 1:
                    if(x==M-1) {
                        continue;
                    }
                    moveRightward(dice);
                    x++;
                    break;
                case 2:
                    if(x==0) {
                        continue;
                    }
                    moveLeftward(dice);
                    x--;
                    break;
                case 3:
                    if(y==0) {
                        continue;
                    }
                    moveUpward(dice);
                    y--;
                    break;
                case 4:
                    if(y==N-1) {
                        continue;
                    }
                    moveDownward(dice);
                    y++;
                    break;
                default:
                    break;
            }
            if (map[y][x] == 0) {
                map[y][x] = dice[3][1];
            } else {
                dice[3][1] = map[y][x];
                map[y][x] = 0;
            }
            // System.out.println(Arrays.deepToString(dice)+ " " + dice[1][1]);
            ret += dice[1][1] + "\n";
        }
        return ret;
    }
    static void moveLeftward(int[][] dice) {
        int temp = dice[1][1];
        dice[1][1] = dice[1][2];
        dice[1][2] = dice[3][1];
        dice[3][1] = dice[1][0];
        dice[1][0] = temp;
    }
    static void moveRightward(int[][] dice) {
        int temp = dice[1][1];
        dice[1][1] = dice[1][0];
        dice[1][0] = dice[3][1];
        dice[3][1] = dice[1][2];
        dice[1][2] = temp;
    }
    static void moveUpward(int[][] dice) {
        int temp = dice[1][1];
        dice[1][1] = dice[2][1];
        dice[2][1] = dice[3][1];
        dice[3][1] = dice[0][1];
        dice[0][1] = temp;
    }
    static void moveDownward(int[][] dice) {
        int temp = dice[1][1];
        dice[1][1] = dice[0][1];
        dice[0][1] = dice[3][1];
        dice[3][1] = dice[2][1];
        dice[2][1] = temp;
    }
}