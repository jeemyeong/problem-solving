import java.io.IOException;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;


public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;

        int n = Integer.parseInt(br.readLine());
        List<Counsel> counsels = new ArrayList<Counsel>();
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            int d = Integer.parseInt(st.nextToken());
            int p = Integer.parseInt(st.nextToken());
            counsels.add(new Counsel(d, p));
        }
        bw.write(solve(n, counsels) + "\n");

        br.close();
        bw.flush();
        bw.close();

    } 
    static int solve(int n, List<Counsel> counsels) {
        int[] dp = new int[n+1];
        for (int i = 0; i < n; i++) {
            Counsel counsel = counsels.get(i);
            dp[i+1] = Math.max(dp[i+1], dp[i]);
            if (i + counsel.d <= n) {
                dp[i + counsel.d] = Math.max(dp[i + counsel.d], dp[i] + counsel.p);
            }
        }
        return dp[n];
    }
    static class Counsel {
        int d;
        int p;
        public Counsel(int d, int p) {
            this.d = d;
            this.p = p;
        }
    }
}