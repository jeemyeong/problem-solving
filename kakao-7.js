// import sys
// sys.setrecursionlimit(25000)

const MAX_INT = 987654321
function solve(strs, t, idx, dp) {
	if (dp.has(idx)) {
		return dp.get(idx);
	}
	let ret = MAX_INT;
	for (let n = idx; n < Math.min(idx+5, t.length); n++) {
		if (strs.has(t.substring(idx, n+1))) {
			ret = Math.min(ret, solve(strs, t, n+1, dp)+1)
		}
	}
	dp.set(idx, ret);
	return ret;


}
function solution(strs, t) {
	const dp = new Map();
	dp.set(t.length, 0)
	const ret = solve(new Set(strs), t, 0, dp);
	if (ret === MAX_INT) {
		return -1
	}
	return ret;
}

console.log(solution(["banan", "n", "a"],"banana")==2)