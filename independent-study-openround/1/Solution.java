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
            int ans = solve(N);
            bw.write(ans + "\n");
        }
        br.close();
        bw.flush();
        bw.close();
    }
    static int solve(int n) {
        if (n < 1000) {
            return n;
        }
        return (n / 1000 * 1000) + ((n / 100)%10 * 10) + ((n / 10)%10 * 100) + n%10;
    }
}