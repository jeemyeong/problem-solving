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
            List<Map<Integer, Integer>> adjList = new ArrayList<Map<Integer, Integer>>();
            for (int j = 0; j <= N; j++) {
                adjList.add(new HashMap<Integer, Integer>());
            }
            for (int j = 0; j < M; j++) {
                st = new StringTokenizer(br.readLine());
                int u = Integer.parseInt(st.nextToken());
                int v = Integer.parseInt(st.nextToken());
                int cost = Integer.parseInt(st.nextToken());
                adjList.get(u).put(v, cost);
                adjList.get(v).put(u, cost);
            }
            int ans = solve(N, M, adjList);
            bw.write(ans + "\n");
        }
        br.close();
        bw.flush();
        bw.close();
    }
    static int solve(int N, int M, List<Map<Integer, Integer>> adjList) {
		PriorityQueue<int[]> heapq = new PriorityQueue<>(new Comparator<int[]>() {
			@Override
			public int compare(int[] o1, int[] o2) {
				return o2[1] - o1[1];
			}
        });
        int ret = 0;
        boolean[] visited = new boolean[N+1];

        for (int i = 1; i<=N; i++) {
            int[] start = {i, 0};
            heapq.add(start);
            int length = 0;
            while (!heapq.isEmpty()) {
                int[] cur = heapq.poll();
                
                if (visited[cur[0]]) {
                    continue;
                }
                visited[cur[0]] = true;
                length += cur[1];
                Map<Integer, Integer> map = adjList.get(cur[0]);
                for (Integer v: map.keySet()) {
                    int[] next = {v, map.get(v)};
                    heapq.add(next);
                }
            }
            ret = Math.max(ret, length);
            break;
        }
        return ret;
    }
}