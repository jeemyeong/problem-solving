MAX_INT = 1e100

function solution(strs, t) {
    const setStrs = new Set(strs);
	const dp = new Map();
    dp.set(0, 0)
    for (let j = 1; j <= t.length; j++) {
        dp.set(j, MAX_INT)
        for (let i = 1; i <= 5; i++) {
            if (j-i < 0) {
                continue;
            }
            if (setStrs.has(t.substring(j-i, j))) {
                dp.set(j, Math.min(dp.get(j), dp.get(j-i)+1))
            }
        }
    }
    const ret = dp.get(t.length)
    
	if (ret === MAX_INT) {
		return -1
    }
	return ret;
}

// console.log(solution(["banan", "n", "a"],"banana")===2)
// console.log(solution(["banan", "n", "a"],"banana")===2)
console.log(solution(["ba", "na", "n", "a"],"banana")===3)
// console.log(solution(["ba", "na", "n", "b"],"b")===1)
// console.log(solution(["app","ap","p","l","e","ple","pp"],"apple")===2)
// console.log(solution(["ba","an","nan","ban","n"],"banana")=== -1)