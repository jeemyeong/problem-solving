package boj.`1000`

import java.io.*
import java.util.*
fun main(args: Array<String>) {
    val br = BufferedReader(InputStreamReader(System.`in`))
    var st: StringTokenizer

    st = StringTokenizer(br.readLine())
    val N = st.nextToken().toInt()
    val M = st.nextToken().toInt()
    val ans = solve(N, M)
    println(ans)
    br.close()
}

fun solve(N: Int, M: Int): Int {

    return N + M
}