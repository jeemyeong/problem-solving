import java.io.BufferedReader
import java.io.IOException
import java.io.InputStreamReader
import java.util.ArrayList
import java.util.Arrays
import java.util.StringTokenizer

internal var N: Int = 0
internal var M: Int = 0
internal var list: Array<ArrayList<Int>> = Array(1001){ArrayList<Int>()}
private var isWork = BooleanArray(1001)
private lateinit var worker: IntArray
private lateinit var working: IntArray

internal class Scan {
    private var tokenizer: StringTokenizer? = null
    private val br: BufferedReader = BufferedReader(InputStreamReader(System.`in`))

    operator fun next(): String {
        while (tokenizer == null || !tokenizer!!.hasMoreTokens()) {
            try {
                tokenizer = StringTokenizer(br.readLine())
            } catch (e: IOException) {
                e.printStackTrace()
            }

        }

        return tokenizer!!.nextToken()
    }

    fun nextInt(): Int {
        return Integer.parseInt(next())
    }

}

fun main(args: Array<String>) {
    val sc = Scan()

    N = sc.nextInt()
    M = sc.nextInt()

    worker = IntArray(1001)
    working = IntArray(1001)

    Arrays.fill(worker, 0, 1001, -1)
    Arrays.fill(working, 0, 1001, -1)
    for (i in 0 until N) {
        list[i] = ArrayList()
        val numWorkings = sc.nextInt()
        for (j in 0 until numWorkings)
            list[i].add(sc.nextInt())
    }

    var cnt = 0
    for (i in 0 until N) {
        if (worker[i] < 0) {
            Arrays.fill(isWork, 0, 1000, false)
            if (dfs(i)) cnt++
        }
    }
    println(cnt)
}

private fun dfs(workerNum: Int): Boolean {
    isWork[workerNum] = true

    for (work in list[workerNum])
        if (working[work] < 0 || !isWork[working[work]] && dfs(working[work])) {
            worker[workerNum] = work
            working[work] = workerNum
            return true
        }


    return false
}
