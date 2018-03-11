package boj.util

import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.*

/**
 * Created by Jeemyeong.
 * User: jeemyeonglee
 * Date: 11/03/2018
 * Time: 8:28 PM
 */
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