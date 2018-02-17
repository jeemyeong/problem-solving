package boj.starter.kotlin

import java.io.*
import java.util.*
import java.util.function.ToIntFunction
import java.util.stream.*


fun main(args: Array<String>) {
    val br = BufferedReader(InputStreamReader(System.`in`))
    var st: StringTokenizer

    val T = br.readLine().toInt()
    for (i in 0 until T) {
        st = StringTokenizer(br.readLine())
        val N = st.nextToken().toInt()
        val M = st.nextToken().toInt()
        val map = Array(N) { IntArray(M) }
        for (j in 0 until N) {
            map[j] = Stream.of(*br.readLine().split(" ".toRegex()).dropLastWhile { it.isEmpty() }.toTypedArray()).mapToInt(ToIntFunction<String> { Integer.parseInt(it) }).toArray()
        }
        val ans = solve(N, M, map)
        println(ans.toString())
    }
    br.close()
}

fun solve(N: Int, M: Int, map: Array<IntArray>): Int {

    return -1
}