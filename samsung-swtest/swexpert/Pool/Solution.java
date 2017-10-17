import java.util.*;
import java.util.stream.*;
import java.io.*;

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;
        
        int T = Integer.parseInt(br.readLine());
        for (int i = 0; i < T; i++) {
            int[] prices = Stream.of(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
            int[] plan = Stream.of(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
            int ans = solve(prices, plan);
            bw.write("#" + (i+1) + " " + ans + "\n");
        }


        bw.flush();
        br.close();
        bw.close();
    }

    static int solve(int[] prices, int[] plan) {
        int[] dp = new int[13];
        for (int i = 1; i < 13; i++) {
            dp[i] = dp[i-1];
            if (plan[i-1] * prices[0] < prices[1]) {
                dp[i] += plan[i-1] * prices[0];
            } else {
                dp[i] += prices[1];
            }
            if (i > 2 && dp[i-3] + prices[2] < dp[i]) {
                dp[i] = dp[i-3] + prices[2];
            }
        }
        if (dp[12] > prices[3]) {
            dp[12] = prices[3];
        }
        return dp[12];
    }
}