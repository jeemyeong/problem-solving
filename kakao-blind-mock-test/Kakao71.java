import java.util.Set;
import java.util.TreeSet;
class Kakao71 {
    int MAX_INT = 987654321;
    public static void main(String[] args) {
        String[] ex_strs = {"ba","na","n","a"};
        String ex_t = "banana";
        Kakao7 instance = new Kakao7();
        int ret = instance.solution(ex_strs, ex_t);
        System.out.println(ret);
    }
	public int solution(String[] strs, String t) {
        Set<String> strsSet = new TreeSet<String>();
        for (String str : strs) {
            strsSet.add(str);
        }
        int[] dp = new int[t.length()+1];
        dp[0] = 0;
        for (int j = 1; j <= t.length(); j++) {
            dp[j] = MAX_INT;
            for (int i = 1; i <= 5; i++) {
                if ((j-i) < 0) {
                    continue;
                }
                if (strsSet.contains(t.substring(j-i, j))) {
                    dp[j] = Math.min(dp[j], dp[j-i]+1);
                }
            }
        }
        int ret = dp[t.length()];
        if (ret == MAX_INT) {
            return -1;
        }
		return ret;
	}
}