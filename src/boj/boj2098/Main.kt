package boj.boj2098

import java.io.*
import java.util.*
import kotlin.math.min

val MAX_VALUE = 987654321

fun main(args: Array<String>) {
    val br = BufferedReader(InputStreamReader(System.`in`))

    val N = br.readLine().toInt()
    var st: StringTokenizer
    val dist = Array(N, {_ -> st = StringTokenizer(br.readLine()); Array(N, {_ -> st.nextToken().toInt()})})
    print(solve(N, dist))
    br.close()
}

fun TSP(cur: Int, visited: Int, cache: Array<Array<Int>>, dist: Array<Array<Int>>, N: Int): Int {
    if (visited == ((1 shl N) - 1)) {
        return dist[cur][0]
    }
    if (cache[cur][visited] != 0) {
        return cache[cur][visited]
    }
    var ret = MAX_VALUE
    for (next in 0 until N) {
        if ((visited and (1 shl next)) > 0) {
            continue
        }
        if (dist[cur][next] == 0) {
            continue
        }
        ret = min(ret, TSP(next, visited or (1 shl next), cache, dist, N) + dist[cur][next] )

    }
    cache[cur][visited] = ret
    return ret
}

fun solve(N: Int, dist: Array<Array<Int>>): Int {
    val cache = Array(N, {_ -> Array(1 shl N, {_ -> 0})})
    return TSP(0, 1, cache, dist, N)

}
