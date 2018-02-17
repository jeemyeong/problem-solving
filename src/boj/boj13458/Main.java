package boj.boj13458;

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
        int N = Integer.parseInt(br.readLine());
        int[] applicants = new int[N];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            int A = Integer.parseInt(st.nextToken());
            applicants[i] = A;
        }
        st = new StringTokenizer(br.readLine());
        int B = Integer.parseInt(st.nextToken());
        int C = Integer.parseInt(st.nextToken());
        bw.write(solve(N, B, C, applicants)+ "\n");
        br.close();
        bw.flush();
        bw.close();
    }
    static long solve(int N, int B, int C, int[] applicants) {
        long ret = N;
        for (int i = 0; i < N; i++) {
            if (applicants[i] <= B) {
                continue;
            }
            applicants[i] -= B;
            ret += applicants[i]/C;
            if (applicants[i] % C > 0) {
                ret += 1;
            }
        }
        return ret;
    }
}