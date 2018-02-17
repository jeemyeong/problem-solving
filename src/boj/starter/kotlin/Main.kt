package boj.starter.kotlin

import java.io.*
import java.util.*
import java.util.function.ToIntFunction
import java.util.stream.*


fun main(args: Array<String>) {
    val br = BufferedReader(InputStreamReader(System.`in`))
    val bw = BufferedWriter(OutputStreamWriter(System.out))
    var st: StringTokenizer

    val T = Integer.parseInt(br.readLine())
    for (i in 0 until T) {
        st = StringTokenizer(br.readLine())
        val N = Integer.parseInt(st.nextToken())
        val M = Integer.parseInt(st.nextToken())
        val map = Array(N) { IntArray(M) }
        for (j in 0 until N) {
            map[j] = Stream.of(*br.readLine().split(" ".toRegex()).dropLastWhile { it.isEmpty() }.toTypedArray()).mapToInt(ToIntFunction<String> { Integer.parseInt(it) }).toArray()
        }
        val ans = solve(N, M, map)
        bw.write(ans.toString() + "\n")
    }
    br.close()
    bw.flush()
    bw.close()
}

fun solve(N: Int, M: Int, map: Array<IntArray>): Int {

    return -1
}