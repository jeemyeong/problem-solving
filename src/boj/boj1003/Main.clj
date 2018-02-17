; ; ; ; ; (defn tail-fibo []
; ; ; ; ;   (cons [1 0] (map first (iterate (fn [[a b]] [b (vec (map +' a b))]) [[0 1] [1 1]]))))
; ; ; ; ; (def lots-of-fibs (take 100000000 (tail-fibo)))
  
; ; ; ; ; (dotimes [n (Integer/parseInt (read-line))]
; ; ; ; ;   (let [[x y] (nth lots-of-fibs (Integer/parseInt (read-line)))]
; ; ; ; ;     (println (format "%d %d" x y))))

; ; ; ; (defn fib [a b m n]
; ; ; ;   (if (= n m) a
; ; ; ;       (recur b (map + a b) (inc m) n)))
; ; ; ; (dotimes [i (read)]
; ; ; ;   (let [n (read)]
; ; ; ;     (apply prn (fib [1 0] [0 1] 0 n))))

; ; ; ; (defn fib-call-count [n]
; ; ; ;   ((nth
; ; ; ;       (iterate 
; ; ; ;           (fn [v]
; ; ; ;               [(v 1) (map + (v 0) (v 1))]
; ; ; ;           )
; ; ; ;       [[1 0] [0 1]]
; ; ; ;       )                    
; ; ; ;       n) 0)
; ; ; ;   )

; ; ; ; (loop [i (read-string (read-line))]
; ; ; ;   (if (> i 0)
; ; ; ;     (let [n (read-string (read-line)) call-count (fib-call-count n)]
; ; ; ;       (println (str (nth call-count 0) " " (nth call-count 1)))
; ; ; ;       (recur (dec i))
; ; ; ;       )
; ; ; ;     )
; ; ; ;   )




; ; (defn fib [n]
; ;   (if (zero? n)
; ;     '(1 0)
; ;     (if (= n 1)
; ;       '(0 1)
; ;       (map +' (fib (dec n)) (fib (- n 2))))))

; ; (def fib (memoize fib))
; ; (def f-seq (map fib (iterate inc 0)))

; ; (loop [i (read-string (read-line))]
; ;   (if (> i 0)
; ;     (let [n (read-string (read-line))]
; ;       (println (str (nth (fib n) 0) " " (nth (fib n) 1)))
; ;       (recur (dec i))
; ;       )
; ;     )
; ;   )


; ; (use '[clojure.string :only (join)])

  
; ; (loop [i (read-string (read-line))]
; ;   (if (> i 0)
; ;     (let [n (read-string (read-line))]
; ;       (println (join " " (nth (fibo) n)))
; ;       (recur (dec i)))))


; (defn fibo []
;   (iterate (fn [[a b]] [b (+ a b)]) [1 0]))

; (dotimes [i (read)]
;   (let [n (read)]
;     (apply prn (nth (fibo) n))))

(defn fib [a b m n]
  (if (= n m) a
      (recur b (map + a b) (inc m) n)))
(dotimes [i (read)]
  (let [n (read)]
    (apply prn (fib [1 0] [0 1] 0 n))))