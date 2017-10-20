import java.io.*;
import java.util.*;
import java.util.stream.Stream;


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
            int C = Integer.parseInt(st.nextToken());
            int[][] map = new int[N][N];
            for (int j = 0; j < N; j++) {
                map[j] = Stream.of(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
            }
            int ans = solve(N, M, C, map);
            bw.write("#" + (i+1) + " " + ans + "\n");
        }
        
        br.close();
        bw.flush();
        bw.close();
    } 

    static int solve(int N, int M, int C, int[][] map) {
        int[][] sumMap = getAllSumByEachPosition(N, M, C, map);
        List<Integer> maxListByRow = new ArrayList<Integer>();
        for (int i = 0; i < N; i++) {
            int max = 0;
            for (int j = 0; j < sumMap[i].length; j++) {
                max = Math.max(max, sumMap[i][j]);
            }
            maxListByRow.add(max);
        }
        Collections.sort(maxListByRow, new Comparator<Integer>(){
            @Override
            public int compare(Integer a, Integer b) {
                return b-a;
            }
        });
        int ans = maxListByRow.get(0) + maxListByRow.get(1);

        for (int i = 0; i < N; i++) {
            for (int j = 0; j <= sumMap[i].length-M; j++) {
                for (int k = j+M; k < sumMap[i].length; k++) {
                    ans = Math.max(ans, sumMap[i][j] + sumMap[i][k]);
                }
            }
        }
        return ans;
    }

    static int[][] getAllSumByEachPosition(int N, int M, int C, int[][] map) {
        int[][] ret = new int[N][N-M+1];
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N-M+1; j++) {
                ret[i][j] = getSumByEachPosition(N, M, C, map, i, j, 0, 0);
            }
        }
        return ret;
    }
    static int getSumByEachPosition(int N, int M, int C, int[][] map, int i, int j, int size, int move) {
        if (j >= N || move >= M) {
            return 0;
        }
        int ret = 0;
        if (map[i][j] <= C - size) {
            ret = Math.max(getSumByEachPosition(N, M, C, map, i, j+1, size, move+1), getSumByEachPosition(N, M, C, map, i, j+1, size+map[i][j], move+1) + map[i][j]*map[i][j]);
        }
        return ret;
    }
}