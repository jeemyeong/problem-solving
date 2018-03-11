//package boj.boj1006
//
//import java.io.BufferedReader
//import java.io.InputStreamReader
//import java.util.StringTokenizer
//import kotlin.math.min
//
//
///**
// * Created by Jeemyeong.
// * User: jeemyeonglee
// * Date: 07/03/2018
// * Time: 12:47 AM
// */
//val MAX_INT = 987654321
//
//fun main(args: Array<String>) {
//    val fc = FastScanner()
//    val t = fc.nextInt()
//    for (i in 0 until t) {
//        val n = fc.nextInt()
//        val w = fc.nextInt()
////        val list = List(2, {List(n, {_ -> fc.nextInt()})
//        val map = List(2, {List(n, {fc.nextInt()})})
//        println(solve(n, w, map))
//    }
//}
//
//fun solve(n: Int, w: Int, map: List<List<Int>>): Int {
//    val dp = Array(2, {Array(n, {Array(3, {Array(4, {MAX_INT})})})})
//    var i = 0
////    if (map[0][0] + map[1][0] <= w) {
////
////    }
//    dp[0][0][0][0] = 0
//    dp[0][0][0][1] = if (map[0][n-1] + map[0][0] <= w) 1 else 2
//    dp[1][0][0] = 0
//    dp[0][0][1] = 1
//    dp[1][0][1] = 1
//    dp[0][0][2] = if (map[0][0] + map[0][1] <= w) 1 else 2
//    dp[1][0][2] = if (map[1][0] + map[1][1] <= w) 1 else 2
//
//    dp[0][1][0] = min()
//    for (j in 1 until n) {
////        println(dp[0][j])
////        dp[i][j] = min(dp[i][j], )
//    }
//    return -1
//}
//
//class FastScanner {
//    var br = BufferedReader(InputStreamReader(System.`in`))
//    var st: StringTokenizer? = null
//    @Throws(Exception::class)
//    fun nextInt(): Int {
//        if (st == null || !st!!.hasMoreTokens()) {
//            st = StringTokenizer(br.readLine())
//        }
//        return Integer.parseInt(st!!.nextToken())
//    }
//}