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
            int K = Integer.parseInt(st.nextToken());
            int A = Integer.parseInt(st.nextToken());
            int B = Integer.parseInt(st.nextToken());
            int[] AList = Stream.of(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
            int[] BList = Stream.of(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
            int[] TList = Stream.of(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
            int ans = solve(N, M, K, A, B, AList, BList, TList);
            bw.write("#" + (i+1) + " " + ans + "\n");
        }
        br.close();
        bw.flush();
        bw.close();
    }
    static int solve(int N, int M, int K, int A, int B, int[] AList, int[] BList, int[] TList) {
        Queue<Customer> receptionQ = new LinkedList<Customer>();
        Queue<Customer> repairQ = new LinkedList<Customer>();
        Queue<Customer> TArrayList = new LinkedList<Customer>();
        int ans = 0;
        for (int i = 0; i < K; i++) {
            TArrayList.add(new Customer(i+1, TList[i]));
        }

        Customer[] receptionCounter = new Customer[N];
        for (int i = 0; i < N; i++) {
            receptionCounter[i] = null;
        }
        Customer[] repairCounter = new Customer[M];
        for (int i = 0; i < M; i++) {
            repairCounter[i] = null;
        }
        
        int t = 0;
        while (!TArrayList.isEmpty() || !receptionQ.isEmpty() || !repairQ.isEmpty() || checkEixst(receptionCounter) || checkEixst(repairCounter)) {
            // 도착한 사람들을 모두 대기열에 넣는다.
            while (!TArrayList.isEmpty() && TArrayList.peek().arriveTime <= t) {
                receptionQ.add(TArrayList.poll());
            }
            
            // 리셉션 끝난 사람들을 리페어 대기열에 넣는다. 모두 기다린 시간을 1초씩 증가시킨다.
            for (int i = 0; i < receptionCounter.length; i++) {
                if (receptionCounter[i] == null) {
                    continue;
                } else if (receptionCounter[i].waitingInReception == (AList[i]-1)) {
                    repairQ.add(receptionCounter[i]);
                    receptionCounter[i] = null;
                } else {
                    receptionCounter[i].waitingInReception += 1;
                }
            }

            // 정비가 끝난 사람들을 모두 꺼낸다. 나머지는 한명씩 증가시킨다.
            for (int i = 0; i < repairCounter.length; i++) {
                if (repairCounter[i] == null) {
                    continue;
                } else if (repairCounter[i].waitingInRepair == (BList[i]-1)) {
                    repairCounter[i] = null;
                } else {
                    repairCounter[i].waitingInRepair += 1;
                }
            }
    
            // 빈 리셉션에 대기열에 있던 사람들을 집어넣는다.
            while (checkEmpty(receptionCounter) != -1 && !receptionQ.isEmpty()) {
                int emptyReceptionDesk = checkEmpty(receptionCounter);
                receptionCounter[emptyReceptionDesk] = receptionQ.poll();
                receptionCounter[emptyReceptionDesk].numberOfReception = emptyReceptionDesk;
            }
    
            // 빈 정비에 대기열에 있던 사람들을 집어넣는다.
            while (checkEmpty(repairCounter) != -1 && !repairQ.isEmpty()) {
                int emptyRepairDesk = checkEmpty(repairCounter);
                repairCounter[emptyRepairDesk] = repairQ.poll();
                repairCounter[emptyRepairDesk].numberOfRepair = emptyRepairDesk;
                if (repairCounter[emptyRepairDesk].numberOfReception == (A-1) && repairCounter[emptyRepairDesk].numberOfRepair == (B-1)) {
                    ans += repairCounter[emptyRepairDesk].number;
                }
            }
            t++;
        }
        if (ans == 0) {
            return -1;
        }
        return ans;
    }

    static int checkEmpty(Customer[] counter) {
        for (int i = 0; i < counter.length; i++) {
            if (counter[i] == null) {
                return i;
            } else {
                continue ;
            }
        }
        return -1;
    }
    static boolean checkEixst(Customer[] counter) {
        for (int i = 0; i < counter.length; i++) {
            if (counter[i] == null) {
                continue;
            } else {
                return true;
            }
        }
        return false;
    }
    static class Customer {
        int number;
        int arriveTime;
        int waitingInReception;
        int waitingInRepair;
        int numberOfReception;
        int numberOfRepair;
        public Customer(int number, int arriveTime) {
            this.number = number;
            this.arriveTime = arriveTime;
        }
        @Override
        public String toString() {
             return "number:" + this.number;
        }
    }
}