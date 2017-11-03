class Solution {
    int MOD = 20170805;
    public static void main(String[] args) {
        Solution drive = new Solution();
        int[][] cityMap1 = {{0, 0, 0}, {0, 0, 0}, {0, 0, 0}};
        int ret = 0;
        // ret = drive.solution(3, 3, cityMap1);
        // System.out.println(ret);
        int[][] cityMap2 =
        {{0, 2, 0, 0, 0, 2},
         {0, 0, 2, 0, 1, 0},
         {1, 0, 0, 2, 2, 0}};
        ret = drive.solution(3, 6, cityMap2);
        System.out.println(ret);
    }

    public int solution(int m, int n, int[][] cityMap) {
        int answer = 0;
        int[][] H = new int[m][n];
        int[][] V = new int[m][n];
        H[0][0] = 1;
        V[0][0] = 1;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (i==0 && j==0) {
                    continue;
                }
                if (cityMap[i][j] == 0) {
                    H[i][j] = (getElementWithoutNullException(H, i, j-1) + getElementWithoutNullException(V, i-1, j))%MOD;
                    V[i][j] = (getElementWithoutNullException(H, i, j-1) + getElementWithoutNullException(V, i-1, j))%MOD;
                } else if (cityMap[i][j] == 2) {
                    H[i][j] = getElementWithoutNullException(H, i, j-1);
                    V[i][j] = getElementWithoutNullException(V, i-1, j);
                }
            }
        }

        return H[m-1][n-1];
    }
    public int getElementWithoutNullException (int[][] map, int i, int j) {
        if (i < 0 || j < 0) {
            return 0;
        } else {
            return map[i][j];
        }
    }
  }