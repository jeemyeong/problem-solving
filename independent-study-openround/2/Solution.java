import java.io.*;
import java.util.*;
import java.util.stream.*;


public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int T = Integer.parseInt(br.readLine());
        for (int i = 0; i < T; i++) {
            int N = Integer.parseInt(br.readLine());
            long ans = solve(N);
            bw.write(ans + "\n");
        }
        br.close();
        bw.flush();
        bw.close();
    }
    static long solve(int n) {
        return (long)n*(n+1) * 3 / 2 - n;
    }
}