package boj.boj15595

import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.StringTokenizer

/**
 * Created by Jeemyeong.
 * User: jeemyeonglee
 * Date: 11/03/2018
 * Time: 8:06 PM
 */
const val adminId = "megalusion"

fun main(args: Array<String>) {
    val submissionList = List(nextInt(), {Submission(nextLong(), next(), nextInt(), nextInt(), nextInt(), nextInt(), nextInt())}).filter{it.userId != adminId}

    val indexedSuccessfulSubmissionMapByUserId = makeIndexedSuccessfulSubmissionMapByUserId(submissionList)

    val successUserCount = indexedSuccessfulSubmissionMapByUserId.count(); if (successUserCount == 0) { println(0); return }
    val submissionBeforeSuccessCount = makeSubmissionBeforeSuccessCount(submissionList, indexedSuccessfulSubmissionMapByUserId)
    val tryCount = successUserCount + submissionBeforeSuccessCount

    println(successUserCount.toDouble()*100/tryCount)
}

val makeIndexedSuccessfulSubmissionMapByUserId: (List<Submission>) -> Map<String, IndexedSubmission> = {
    it.mapIndexed{index: Int, submission -> IndexedSubmission(index, submission)}
    .filter{ isSuccessfulSubmission(it.submission) }
    .groupBy{it.submission.userId}
    .mapValues { it.value[0] }
}
val makeSubmissionBeforeSuccessCount: (List<Submission>, Map<String, IndexedSubmission>) -> Int = {
    submissionList, indexedSuccessfulSubmissionMapByUserId ->
    submissionList.filterIndexed{index: Int, submission -> isBeforeThanSuccess(index, submission, indexedSuccessfulSubmissionMapByUserId)}
    .filter{isNotSuccessfulSubmission(it)}
    .count()
}
val isSuccessfulSubmission: (Submission) -> Boolean = {it.result == 4}
val isNotSuccessfulSubmission: (Submission) -> Boolean = {!isSuccessfulSubmission(it)}
val isSuccessfulUser: (Submission, Map<String, IndexedSubmission>) -> Boolean = { submission, indexedSuccessfulSubmissionMapByUserId ->  submission.userId in indexedSuccessfulSubmissionMapByUserId.keys}
val isBeforeThanSuccess: (Int, Submission, Map<String, IndexedSubmission>) -> Boolean = {
    index, submission, indexedSuccessfulSubmissionMapByUserId ->
        isSuccessfulUser(submission, indexedSuccessfulSubmissionMapByUserId) && index < indexedSuccessfulSubmissionMapByUserId[submission.userId]!!.index
}

data class IndexedSubmission(val index: Int, val submission: Submission)

data class Submission(val number: Long, val userId: String, val result: Int, val usedMemorySize: Int, val operatingTime: Int, val language: Int, val codeSize: Int)

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
val nextInt: () -> Int = { next().toInt() }
val nextLong: () -> Long = { next().toLong() }