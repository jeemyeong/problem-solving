package boj.boj10217

import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.*

fun solve(n: Int, m: Int, k: Int, arrayOfRoutes: List<Routes>): String {
    val q = PriorityQueue<Point>(Comparator<Point> { x, y -> x.totalDuration - y.totalDuration })
    q.add(Point(1, 0, 0))
    val visited = List(n+1) {HashSet<Point>()}
    fun isExpensiveThanAnyPointsInSet(set: Set<Point>, point: Point): Boolean {
        if (set.isEmpty()) {
            return false
        }
        set.forEach {
            if (it.totalCost < point.totalCost && it.totalDuration < point.totalDuration) {
                return true
            }
        }
        return false
    }
    while (!q.isEmpty()) {
        val cur = q.poll()
        if (cur.totalCost > m) {
            continue
        }
        if (cur.position == n) {
            return cur.totalDuration.toString()
        }

        arrayOfRoutes[cur.position].routes.forEach{
            val next = Point(it.To, cur.totalCost + it.cost, cur.totalDuration + it.duration)
            if (!isExpensiveThanAnyPointsInSet(visited[it.To], next)) {
                q.add(next)
                visited[it.To].add(next)
            }
        }
    }
    return "Poor KCM"
}

fun main(args: Array<String>) {
    for (iter in 0 until next().toInt()){
        val n = next().toInt(); val m = next().toInt(); val k = next().toInt()
        val arrayOfRoutes = List(n+1){ i -> Routes(i)}
        for (i in 0 until k) {
            val from = next().toInt()
            arrayOfRoutes[from].add(Route(from, next().toInt(), next().toInt(), next().toInt()))
        }
        println(solve(n, m, k, arrayOfRoutes))
    }
}
class Routes(val from: Int, val routes: HashSet<Route> = HashSet()) {
    fun add(route: Route) {
        routes.add(route)
    }
}
data class Route(val from: Int, val To: Int, val cost: Int, val duration: Int)
data class Point(val position: Int, val totalCost: Int, val totalDuration: Int)

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
