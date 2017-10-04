import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;
import java.util.Arrays;
import java.util.ArrayList;
import java.util.Stack;
import java.util.Queue;
import java.util.LinkedList;
import java.util.List;
import java.util.HashMap;
import java.util.HashSet;

public class Main {
    static int INF = 2000000000;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;
        int L = Integer.parseInt(br.readLine());
        int N = Integer.parseInt(br.readLine());
        Queue<TurnDirection> turnDirections = new LinkedList<TurnDirection>();
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            int t = Integer.parseInt(st.nextToken());
            char dir = st.nextToken().charAt(0);
            turnDirections.add(new TurnDirection(t, dir));
        }
        bw.write(solve(N, L, turnDirections)+ "\n");
        br.close();
        bw.flush();
        bw.close();
    }
    
    static long solve(int N, int L, Queue<TurnDirection> turnDirections) {
        Point head = new Point(L, L);

        // Directions
        int downward = 0;
        int rightward = 1;
        int leftward = 0;
        int upward = 0;

        // Lines should be added into list
        List<Line> lineList = new ArrayList<Line>();

        // return should be long type
        long ret = 0;

        // This is last line to bump into wall in final
        turnDirections.add(new TurnDirection(2*L+1, 'L'));

        while (true) {
            TurnDirection nextTurnDirection = turnDirections.poll();
            int length = nextTurnDirection.t;
            char type;
            if (rightward == 1 || leftward == 1) {
                type = 'H';
            } else {
                type = 'V';
            }
            Point nextHead = new Point(head.y+(downward-upward)*length, head.x+(rightward-leftward)*length);
            Line line = new Line(head, nextHead, type);
            int lineListSize = lineList.size();

            // Check there are conflicts with other lines
            int conflict = INF;
            for (int j = 0; j < lineListSize - 1; j++) {
                Line otherLine = lineList.get(j);
                if (line.type == 'H' && otherLine.type == 'H') {
                    if (line.p1.y != otherLine.p1.y) {
                        continue;
                    } else if (line.p1.x < Math.min(otherLine.p1.x, otherLine.p2.x) && line.p2.x < Math.min(otherLine.p1.x, otherLine.p2.x)) {
                        continue;
                    } else if (line.p1.x > Math.max(otherLine.p1.x, otherLine.p2.x) && line.p2.x > Math.max(otherLine.p1.x, otherLine.p2.x)) {
                        continue;
                    }
                    
                    // Found conflict
                    if (rightward == 1) {
                        conflict = Math.min(conflict, Math.min(otherLine.p1.x, otherLine.p2.x)-head.x);
                    } else if (leftward == 1) {
                        conflict = Math.min(conflict, head.x - Math.max(otherLine.p1.x, otherLine.p2.x));
                    }
                } else if (line.type == 'V' && otherLine.type == 'V') {
                    if (line.p1.x != otherLine.p1.x) {
                        continue;
                    } else if (line.p1.y < Math.min(otherLine.p1.y, otherLine.p2.y) && line.p2.y < Math.min(otherLine.p1.y, otherLine.p2.y)) {
                        continue;
                    } else if (line.p1.y > Math.max(otherLine.p1.y, otherLine.p2.y) && line.p2.y > Math.max(otherLine.p1.y, otherLine.p2.y)) {
                        continue;
                    }

                    // Found conflict
                    if (downward == 1) {
                        conflict = Math.min(conflict, Math.min(otherLine.p1.y, otherLine.p2.y)-head.y);
                    } else if (upward == 1) {
                        conflict = Math.min(conflict, head.y - Math.max(otherLine.p1.y, otherLine.p2.y));
                    }
                } else if (line.type == 'H' && otherLine.type == 'V') {
                    if (line.p1.y < Math.min(otherLine.p1.y, otherLine.p2.y) || line.p1.y > Math.max(otherLine.p1.y, otherLine.p2.y)) {
                        continue;
                    } else if (otherLine.p1.x < Math.min(line.p1.x, line.p2.x) || otherLine.p1.x > Math.max(line.p1.x, line.p2.x)) {
                        continue;
                    }

                    // Found conflict
                    conflict = Math.min(conflict, Math.abs(otherLine.p1.x-head.x));
                } else if (line.type == 'V' && otherLine.type == 'H') {
                    if (line.p1.x < Math.min(otherLine.p1.x, otherLine.p2.x) || line.p1.x > Math.max(otherLine.p1.x, otherLine.p2.x)) {
                        continue;
                    } else if (otherLine.p1.y < Math.min(line.p1.y, line.p2.y) || otherLine.p1.y > Math.max(line.p1.y, line.p2.y)) {
                        continue;
                    }

                    // Found conflict
                    conflict = Math.min(conflict, Math.abs(otherLine.p1.y-head.y));
                }
            }

            // If conflict is found, return ret + conflict
            if (conflict != INF) {
                return ret + conflict;
            }

            // Snake bumped into wall
            if (nextHead.y < 0 || nextHead.x < 0 || nextHead.x > 2*L || nextHead.y > 2*L) {
                if (rightward == 1) {
                    return ret + 2*L - head.x + 1;
                } else if (leftward == 1) {
                    return ret + head.x + 1;
                } else if (upward == 1) {
                    return ret + head.y + 1;
                } else if (downward == 1) {
                    return ret + 2*L - head.y + 1;
                }
            }

            // Go along
            lineList.add(line);
            ret += length;
            if (nextTurnDirection.dir == 'L') {
                int temp = rightward;
                rightward = downward;
                downward = leftward;
                leftward = upward;
                upward = temp;
            } else if (nextTurnDirection.dir == 'R') {
                int temp = rightward;
                rightward = upward;
                upward = leftward;
                leftward = downward;
                downward = temp;
            }

            // Head should be changed
            head = nextHead;
        }
    }

    static class Point {
        int y, x;
        public Point(int y, int x) {
            this.y = y;
            this.x = x;
        }
        public void print() {
            System.out.print("y: ");
            System.out.print(y);
            System.out.print(", x: ");
            System.out.println(x);
        }
    }
    static class Direction {
        int y, x;
        public Direction(int y, int x) {
            this.y = y;
            this.x = x;
        }
    }
    static class TurnDirection {
        int t;
        char dir;
        public TurnDirection(int t, char dir) {
            this.t = t;
            this.dir = dir;
        }
    }
    static class Line {
        Point p1, p2;
        char type;
        public Line(Point p1, Point p2, char type) {
            this.p1 = p1;
            this.p2 = p2;
            this.type = type;
        }
        public void print() {
            this.p1.print();
            this.p2.print();
            System.out.println(type);
            System.out.println();
        }
    }
}