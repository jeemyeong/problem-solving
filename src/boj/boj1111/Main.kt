package boj.boj1111

import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.*
import java.util.stream.Collectors.toList

fun main(args: Array<String>) {
    val br = BufferedReader(InputStreamReader(System.`in`))
    val n = br.readLine().toInt()
    val st = StringTokenizer(br.readLine())
    var lst = (0 until n).toList()
    lst = lst.stream().map({st.nextToken().toInt()}).collect(toList())

    var a = 0
    var b = 0

    if (lst.size >= 3) {
        if (lst[1] - lst[0] != 0) {
            a = (lst[2] - lst[1]) / (lst[1] - lst[0])

        } else {
            a = 1
        }
        b = lst[1]-a*lst[0]
    }

    var p = true
    for (i in 1 until lst.size) {
        if (lst[i] != (lst[i-1]*a+b)) {
            p = false
            break
        }
    }

    if(lst.size<3) {
        if((lst.size==2&&lst[1]!=lst[0])||lst.size==1) {
            println("A")
        } else {
            println(lst[0])
        }
    } else if (p == true) {
        println(a*lst[lst.size-1]+b)
    } else {
        println("B")
    }
}
