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
    map.forEach { println(); it.forEach { print(if (it) "T\t" else "F\t") } }; println()
    println(solve(map))
}

fun solve(map: Array<Array<Boolean>>): Int {
    return -1
}

//fun dfs()
    
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
