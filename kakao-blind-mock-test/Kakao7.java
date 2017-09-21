import java.util.Set;
import java.util.TreeSet;
class Kakao7 {
    int MAX_INT = 987654321;
    public static void main(String[] args) {
        String[] ex_strs = {"ba","na","n","a"};
        String ex_t = "banana";
        Kakao7 instance = new Kakao7();
        int ret = instance.solution(ex_strs, ex_t);
        System.out.println(ret);
    }
    public int solve(Set strs, String t, int idx, int[] dp) {
        if (dp[idx] != -1) {
            return dp[idx];
        }
        dp[idx] = MAX_INT;
        for (int n = idx; n < Math.min(idx+5, t.length()); n++) {
            if (strs.contains(t.substring(idx, n+1))) {
                dp[idx] = Math.min(dp[idx], solve(strs, t, n+1, dp)+1);
            }
        }
        return dp[idx];
    }
	public int solution(String[] strs, String t) {
        Set<String> strsSet = new TreeSet<String>();
        for (String str : strs) {
            strsSet.add(str);
        }
        int[] dp = new int[t.length()+1];
        for (int i = 0; i < dp.length; i++) {
            dp[i] = -1;
        }
        dp[t.length()] = 0;
        int ret = solve(strsSet, t, 0, dp);
        if (ret == MAX_INT) {
            return -1;
        }
		return ret;
	}
}