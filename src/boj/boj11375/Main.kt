package boj.boj11375

import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.*

/**
 * Created by Jeemyeong.
 * User: jeemyeonglee
 * Date: 14/03/2018
 * Time: 12:40 AM
 */

fun main(args: Array<String>) {
    val n = next().toInt()
    val m = next().toInt()
    val map = Array(n){Array(m){false}}
    map.forEach { row ->
        for (y in 0 until next().toInt()) {
            row[next().toInt()-1] = true
        }
    }
    fun solve(): Int {
        var visit = Array(n) {false}
        val visited = Array(m, {-1})
        fun dfs(i: Int): Int {
            if (visit[i]) {
                return 0
            }
            visit[i] = true
            for (j in 0 until m) {
                if (!map[i][j]) continue
                if (visited[j] == -1) {
                    visited[j] = i
                    return 1
                }
                if (dfs(visited[j]) == 1) {
                    visited[j] = i
                    return 1
                }
            }
            return 0
        }
        var ret = 0
        for (i in 0 until n) {
            visit = Array(n) {false}
            ret += dfs(i)
        }
        return ret
    }
    println(solve())
}

class FastScanner {
    var br = BufferedReader(InputStreamReader(System.`in`))
    var st: StringTokenizer? = null
    @Throws(Exception::class)
    fun next(): String {
        if (st == null || !st!!.hasMoreTokens()) {
            st = StringTokenizer(br.readLine())
        }
        return st!!.nextToken()
    }
}
val fc = FastScanner()
val next: () -> String = { fc.next() }
