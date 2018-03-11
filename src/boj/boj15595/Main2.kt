//package boj.boj15595
//
//import java.io.BufferedReader
//import java.io.InputStreamReader
//import java.util.*
//import kotlin.collections.HashMap
//
///**
// * Copy of https://www.acmicpc.net/source/7964800
// * Thanks to jh05013
// */
//
//
//fun main(args: Array<String>) {
//    val n = nextInt()
//    val ac = HashMap<String, Int>()
//    val wa = HashMap<String, Int>()
//
//    for (i in 0 until n) {
//        val submission = Submission(nextLong(), next(), nextInt(), nextInt(), nextInt(), nextInt(), nextInt())
//        val (no, user, res, mem, time, lang, length) = submission
//        if (user == "megalusion") continue
//        if (user in ac) continue
//        if (res == 4) ac[user] = if (wa.containsKey(user)) wa[user]!! + 1  else 1
//        else wa[user] = if (wa.containsKey(user)) wa[user]!! + 1  else 1
//    }
//    if (ac.size == 0) println(0)
//    else println(ac.size.toDouble() / ac.values.sum() * 100)
//}
//
//data class Submission(val number: Long, val userId: String, val result: Int, val usedMemorySize: Int, val operatingTime: Int, val language: Int, val codeSize: Int)
//
//class FastScanner {
//    var br = BufferedReader(InputStreamReader(System.`in`))
//    var st: StringTokenizer? = null
//    @Throws(Exception::class)
//    fun next(): String {
//        if (st == null || !st!!.hasMoreTokens()) {
//            st = StringTokenizer(br.readLine())
//        }
//        return st!!.nextToken()
//    }
//}
//val fc = FastScanner()
//val next: () -> String = { fc.next() }
//val nextInt: () -> Int = { next().toInt() }
//val nextLong: () -> Long = { next().toLong() }