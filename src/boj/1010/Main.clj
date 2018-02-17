(dotimes [i (Integer/parseInt (read-line))]
  (let [nums (map #(Integer/parseInt %) (.split (read-line) " "))]
    (apply prn nums)))
  ;   ; (apply prn (fib [1 0] [0 1] 0 n))))