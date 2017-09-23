import java.util.Scanner;
import java.util.Arrays;

class TransposedMatrix {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int N = Integer.parseInt(scan.nextLine());
        int[][] map = new int[N][N];
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                map[i][j] = scan.nextInt();
            }
        }
        for (int i = 0; i < N; i++) {
            for (int j = i+1; j < N; j++) {
                int temp = map[i][j];
                map[i][j] = map[j][i];
                map[j][i] = temp;
            }
        }
        for (int[] row : map) {
            for (int i = 0; i < N; i++) {
                if (i == N-1) {
                    System.out.println(row[i]);
                }
                else {
                    System.out.print(row[i] + " ");
                }
            }
        }
        scan.close();
    }
}
    