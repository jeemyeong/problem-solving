import java.util.Collections;
import java.util.Scanner;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;

class AttachNumber {
    
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String[] inputs = scan.nextLine().split(" ");
        ArrayList<Integer> origin = new ArrayList<Integer>();
        for (String eachString : inputs) {
            origin.add(Integer.parseInt(eachString));
        }
        ArrayList<Integer> result = new ArrayList<Integer>();

        Queue<DSForPermutation> q = new LinkedList<DSForPermutation>();
        q.add(new DSForPermutation(origin, ""));
        while (q.size() > 0) {
            DSForPermutation cur = q.poll();

            if (cur.list.size() == 0) {
                result.add(Integer.parseInt(cur.number));
                continue;
            }

            int n = cur.list.size();
            for (int i = 0; i < n; i++) {
                ArrayList<Integer> curList = new ArrayList<Integer>();
                String curNumber = new String(cur.number);
                for (int j = 0; j < n; j++) {
                    if (i == j) {
                        curNumber += cur.list.get(j);
                        continue;
                    }
                    curList.add(cur.list.get(j));
                }
                q.add(new DSForPermutation(curList, curNumber));
            }
        }
        int minNumber = Collections.min(result);
        int maxNumber = Collections.max(result);
        System.out.println(minNumber + maxNumber);
    }
}
    
class DSForPermutation {
    String number;
    ArrayList<Integer> list;
    DSForPermutation(ArrayList<Integer> list, String number) {
        this.list = list;
        this.number = number;
    }
}