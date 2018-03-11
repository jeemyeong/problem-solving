package boj.boj1309

import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.*

/**
 * Created by Jeemyeong.
 * User: jeemyeonglee
 * Date: 12/03/2018
 * Time: 1:02 AM
 */

fun main(args: Array<String>) {
    val n = next().toInt()
    val dp = Array(n, {Row()})
    dp[0].left = 1
    dp[0].right = 1
    dp[0].empty = 1
    for (i in 1 until n) {
        dp[i].left = (dp[i-1].empty + dp[i-1].right) % 9901
        dp[i].right = (dp[i-1].empty + dp[i-1].left) % 9901
        dp[i].empty = (dp[i-1].left + dp[i-1].right + dp[i-1].empty) % 9901
    }
    println((dp[n-1].left + dp[n-1].right + dp[n-1].empty) % 9901)
}

data class Row(var left: Long = 0, var right: Long = 0, var empty: Long = 0)

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
