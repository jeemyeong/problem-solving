package boj.boj2800

import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.*
import kotlin.collections.HashSet

/**
 * Created by Jeemyeong.
 * User: jeemyeonglee
 * Date: 17/03/2018
 * Time: 2:20 PM
 */

//fun main(args: Array<String>) {
//    val cache = HashMap<String, Set<String>>()
//    fun splitParenthesis(input: String): List<String> {
//        val stack = Stack<Char>()
//        var lastSplitedPointer = 0
//        val ret: ArrayList<String> = ArrayList()
//        for (curPointer in 0 until input.length) {
//            if (input[curPointer] == '(') {
//                if (stack.empty() && lastSplitedPointer != curPointer) {
//                    ret.add(input.substring(lastSplitedPointer, curPointer))
//                    lastSplitedPointer = curPointer
//                }
//                stack.push(input[curPointer])
//                continue
//            }
//            if (input[curPointer] == ')') {
//                stack.pop()
//                if (stack.empty()) {
//                    ret.add(input.substring(lastSplitedPointer, curPointer+1))
//                    lastSplitedPointer = curPointer+1
//                }
//                continue
//            }
//        }
//        if (lastSplitedPointer != input.length) {
//            ret.add(input.substring(lastSplitedPointer, input.length))
//        }
//        return ret
//    }
//    fun parenthesisCases(input: String): Set<String> {
//        if (cache.containsKey(input)) {
//            return cache[input] as Set<String>
//        }
//        var ret = HashSet<String>()
//        ret.add("")
//        splitParenthesis(input).forEach {
//            parenthesis ->
//                if (parenthesis.first() == '(' && parenthesis.last() == ')' && parenthesis.length > 2) {
//                    val newRet = HashSet<String>()
//                    parenthesisCases(parenthesis.substring(1, parenthesis.lastIndex)).forEach{
//                        case -> ret.forEach{
//                            origin ->
//                                newRet.add(origin + case)
//                                newRet.add(origin + "(" + case + ")")
//                        }
//                    }
//                    ret.forEach{
//                        origin -> newRet.add(origin + parenthesis)
//                    }
//                    ret = newRet
//                } else {
//                    ret = ret.map { it.plus(parenthesis) }.toHashSet()
//                }
//        }
//        cache[input] = ret
//        return ret
//    }
//
//    val input = next()
//    parenthesisCases(input).sorted().forEach {
//        if (it != input) {
//            println(it)
//        }
//    }
//}

fun solve(str: String): Set<String> {
    val stack = Stack<Int>()
    for (cur in 0 until str.length) {
        when {
            str[cur] == '(' -> {
                stack.push(cur)
            }
            str[cur] == ')' && stack.size > 1 -> {
                stack.pop()
            }
            str[cur] == ')' && stack.size == 1 -> {
                val start = stack.pop()
                val front = str.substring(0, start)
                val middles = solve(str.substring(start+1, cur))
                val backs = solve(str.substring(cur+1, str.length))
                val ret = HashSet<String>()
                middles.forEach{ middle ->
                    backs.forEach{ back ->
                        ret.add("$front($middle)$back")
                        ret.add("$front$middle$back")
                    }
                }
                return ret
            }
        }
    }
    val ret = HashSet<String>()
    ret.add(str)
    return ret
}
fun main(args: Array<String>) {
    val input = next()
    val ret = solve(input).minus(input).sorted()
    println(ret.joinToString("\n"))
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
