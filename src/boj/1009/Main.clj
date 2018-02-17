(defn square [n] (* n n))
(defn f [a b]
  (cond (= (rem a 10) 1) (rem a 10)
        (= (rem a 10) 5) (rem a 10)
        (= (rem a 10) 6) (rem a 10)
        (= (rem a 10) 0) (rem a 0)
        (= (even? b) 0) (f (square a), (/ b 2))
        :else (rem (* (f (square a), (quot b 2)) a) 10)))
(defn g [x]
  (if (= x 0) 10 x))
(dotimes [n (read)]
  (println (g (f (read) (read)))))