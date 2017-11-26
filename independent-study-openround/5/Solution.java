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
            st = new StringTokenizer(br.readLine());
            int[] R = new int[N+1];
            for (int j = 1; j < N+1; j++) {
                R[j] = Integer.parseInt(st.nextToken());
            }
            List<Map<Integer, Integer>> adjList = new ArrayList<Map<Integer, Integer>>();
            for (int j = 0; j <= N; j++) {
                adjList.add(new HashMap<Integer, Integer>());
            }
            for (int j = 0; j < M; j++) {
                st = new StringTokenizer(br.readLine());
                int u = Integer.parseInt(st.nextToken());
                int v = Integer.parseInt(st.nextToken());
                int cost = Integer.parseInt(st.nextToken());
                if (adjList.get(u).containsKey(v)) {
                    adjList.get(u).put(v, Math.min(cost, adjList.get(u).get(v)));
                } else {
                    adjList.get(u).put(v, cost);
                }
                if (adjList.get(v).containsKey(u)) {
                    adjList.get(v).put(u, Math.min(cost, adjList.get(v).get(u)));
                } else {
                    adjList.get(v).put(u, cost);
                }
            }
            int ans = solve(N, M, adjList, R);
            bw.write(ans + "\n");
        }
        br.close();
        bw.flush();
        bw.close();
    }
    static int solve(int N, int M, List<Map<Integer, Integer>> adjList, int[] R) {
		PriorityQueue<int[]> heapq = new PriorityQueue<>(new Comparator<int[]>() {
			@Override
			public int compare(int[] o1, int[] o2) {
				return o1[1] - o2[1];
			}
        });
        int MAX_INT = 987654321;
        int[] visited = new int[N+1];
        for (int i = 0; i < visited.length; i++) {
            visited[i] = MAX_INT;
        }
        visited[1] = 0;

        int[] cur = {1, R[1]};
        visited[1] = R[1];
        heapq.add(cur);
        while (!heapq.isEmpty()) {
            cur = heapq.poll();
            Map<Integer, Integer> map = adjList.get(cur[0]);
            for (Integer v: map.keySet()) {
                if (visited[v] > cur[1] + map.get(v) + R[v]) {
                    visited[v] = cur[1] + map.get(v) + R[v];
                    int[] next = {v, visited[v]};
                    heapq.add(next);
                }
            }
        }
        int ret = 0;
        for (int i = 1; i < N+1; i++) {
            if (visited[i] != MAX_INT){
                ret += visited[i];
            }
        }
        return ret;
    }
}