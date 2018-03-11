package boj.boj1546

import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.StringTokenizer

fun main(args: Array<String>) {
    val fc = FastScanner()
    val n = fc.next().toInt()
    val scores = List(n, {nextInt()})
    println("%.2f".format(scores.sum().toDouble()*100/n/scores.max() as Int))
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
val fc = boj.boj15595.FastScanner()
val next: () -> String = { fc.next() }
val nextInt: () -> Int = { next().toInt() }
