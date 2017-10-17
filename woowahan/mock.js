// you can write to stdout for debugging purposes, e.g.
// console.log('this is a debug message');

function solution(A) {
    // write your code in JavaScript (Node.js 6.4.0)
    set = new Set();
    for (var i = 0; i < A.length; i++) {
        set.add(A[i]);
    }
    for (var i = 1; i < 100002; i++) {
        if (set.has(i)) {
            continue;
        } else {
            return i;
        }
    }

}

solution([1, 3, 6, 4, 1, 2])